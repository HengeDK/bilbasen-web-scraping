import constants.listing_anchors as ANCHOR_TYPE
import constants.listing_description_types as DESCRIPTION_TYPE
import constants.listing_car_specifications as SPECIFICATIONS_TYPE
import constants.listing_price_types as PRICE_TYPE
import constants.listing_location_types as LOCATION_TYPE
from helpers import format_kml_str, format_kmt_str, format_price_str
from decimal import Decimal
from collections import namedtuple
import simplejson as json

Car = namedtuple('Car', 'model link description kms year hk kml kmt moth trailer location price')


def extract_car_info(html_containers):
    cars = []

    for container in html_containers:
        anchor = container.find("a", {"class": ANCHOR_TYPE.CONST_CAR_LISTING_MAIN_ANCHOR()})

        model = anchor.string
        link = anchor["href"]
        description = container.find("div", {"class": DESCRIPTION_TYPE.CONST_DESCRIPTION_TYPE()}).string or "NO_DESCRIPTION"
        if description is not "NO_DESCRIPTION" and description is not None and description is not "":
            description = description.replace("'", "''")

        specifications = container.findAll("div", {"class": SPECIFICATIONS_TYPE.CONST_CAR_SPECIFICATIONS()})
        unpredictable_specifications = container.find("span", {
            "class": SPECIFICATIONS_TYPE.CONST_CAR_UNPREDICTABLE_SPECIFICATIONS()})

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
        price = format_price_str(container.find("div", {"class", PRICE_TYPE.CONST_PRICE_DIV()}).string)
        location = container.find("div", {"class": LOCATION_TYPE.CONST_LOCATION_DIV()}).string

        car = Car(model, link, description, kms, year, hk, kml, kmt, moth, trailer, location, price)
        cars.append(car)

    file = open("cars.json", "w+")
    file.write(json.dumps(cars))
    file.close()
