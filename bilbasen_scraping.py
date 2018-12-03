import constants.listing_anchors as anchor_type
import constants.listing_description_types as descriptions_type
import constants.listing_car_specifications as specifications_type
import constants.listing_price_types as price_type
import constants.listing_location_types as location_type
from helpers import format_kml_str, format_kmt_str, format_price_str
from decimal import Decimal
from collections import namedtuple
from database import insert_brand
from xmltodict import parse
from urllib.request import urlopen as http_req
from bilbasen_soup import get_soup_for_car_extraction, get_soup_for_pages_extraction
import database as db
from constants.pagination_types import CONST_PAGINATION_LISTINGS_TYPE
import constants.bilbasen_urls as url_types

Car = namedtuple('Car', 'model link description kms year hk kml kmt moth trailer location price')


def get_count_of_pages():
    soup = get_soup_for_pages_extraction()
    uls = soup.find("ul", {"class": CONST_PAGINATION_LISTINGS_TYPE()})

    highest = 0
    lis = uls.findAll("li")

    for li in lis:
        if li.text != "<" and li.text != "":
            text = li.text.replace(".", "")
            if int(text) > highest:
                highest = int(text)

    return highest


def start_scraping_cars(page_limit):
    page_limit = int(page_limit)
    if page_limit == 0:
        page_limit = get_count_of_pages()

    page_arr = list(range(1, page_limit + 1))
    for page_num in page_arr:
        print(f"Scraping page: {page_num}")
        soup = get_soup_for_car_extraction(page_num)
        extract_car_info(soup)


def extract_car_info(html_containers):
    for container in html_containers:
        anchor = container.find("a", {"class": anchor_type.CONST_CAR_LISTING_MAIN_ANCHOR()})

        model = anchor.string
        link = anchor["href"]

        description = container.find("div", {"class": descriptions_type.CONST_DESCRIPTION_TYPE()})
        if description:
            description = description.string
        else:
            description = "NO_DESCRIPTION"
        if description is not "NO_DESCRIPTION" and description is not None and description is not "":
            description = description.replace("'", "''")
        description = description.strip()

        specifications = container.findAll("div", {"class": specifications_type.CONST_CAR_SPECIFICATIONS()})
        unpredictable_specifications = container.find("span", {
            "class": specifications_type.CONST_CAR_UNPREDICTABLE_SPECIFICATIONS()})

        hk = unpredictable_specifications["data-hk"]
        kms = int(specifications[1].string.replace(".", ""))
        year = int(specifications[2].string)
        kml = format_kml_str(unpredictable_specifications["data-kml"])
        if kml is not "":
            kml = Decimal(kml)

        kmt = format_kmt_str(unpredictable_specifications["data-kmt"])
        if kmt is not "":
            kmt = Decimal(kmt)

        moth = unpredictable_specifications["data-moth"]
        trailer = unpredictable_specifications["data-trailer"]
        price = format_price_str(container.find("div", {"class", price_type.CONST_PRICE_DIV()}).string)
        location = container.find("div", {"class": location_type.CONST_LOCATION_DIV()}).string

        car = Car(model, link, description, kms, year, hk, kml, kmt, moth, trailer, location, price)
        db.insert_car(car)


def extract_car_brands_and_fill_table():
    url = url_types.CONST_CAR_BRANDS_URL()
    u_client = http_req(url)
    xml = u_client.read()
    u_client.close()

    parsed = parse(xml)
    dicts = parsed["Makes"]["Make"]

    for di in dicts:
        if any(char.isalpha() for char in di["Name"]):
            insert_brand(di["Name"])
