from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import constants.listing_types as AD_TYPE
import time

def get_soup_for_car_extraction(page_number):
    url = f"https://www.bilbasen.dk/brugt/bil?Fuel=0&YearFrom=0&YearTo=0&PriceFrom=0&PriceTo=10000000&MileageFrom=-1&MileageTo=10000001&IncludeEngrosCVR=true&IncludeLeasing=true&page={page_number}"
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class": AD_TYPE.CONST_PLUS_AD_TYPE()})
    return containers


def get_soup_for_pages_extraction():
    url = "https://www.bilbasen.dk/brugt/bil?Fuel=0&YearFrom=0&YearTo=0&PriceFrom=0&PriceTo=10000000&MileageFrom=-1&MileageTo=10000001&IncludeEngrosCVR=true&IncludeLeasing=true&page=99999"
    uClient = uReq(url)
    max_url = uClient.geturl()
    uClient.close()


    maxClient = uReq(max_url)
    page_html = maxClient.read()
    maxClient.close()
    page_soup = soup(page_html, "html.parser")
    return page_soup




