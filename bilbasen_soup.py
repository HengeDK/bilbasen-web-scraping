from urllib.request import urlopen as http_req
from bs4 import BeautifulSoup as Soup
import constants.listing_types as ad_type
import constants.bilbasen_urls as url_types


def get_soup_for_car_extraction(page_number):
    url = url_types.CONST_CAR_LISTINGS_VARIABLE_PAGE_NUMBER(page_number)
    u_client = http_req(url)
    page_html = u_client.read()
    u_client.close()
    page_soup = Soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class": {ad_type.CONST_PLUS_AD_TYPE(), ad_type.CONST_PLUS_DISCOUNT_TYPE(), ad_type.CONST_PLUS_EXCLUSIVE_TYPE()}})
    return containers


def get_soup_for_pages_extraction():
    url = url_types.CONST_CAR_LISTINGS_MAX_PAGE()
    u_client = http_req(url)
    max_url = u_client.geturl()
    u_client.close()

    max_client = http_req(max_url)
    page_html = max_client.read()
    max_client.close()
    page_soup = Soup(page_html, "html.parser")
    return page_soup




