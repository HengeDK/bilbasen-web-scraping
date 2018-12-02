from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import constants.listing_types as AD_TYPE
import simplejson as json
from xmltodict import parse
import codecs



def get_soup_for_car_extraction(page_number):
    url = f"https://www.bilbasen.dk/brugt/bil?Fuel=0&YearFrom=0&YearTo=0&PriceFrom=0&PriceTo=10000000&MileageFrom=-1&MileageTo=10000001&IncludeEngrosCVR=true&IncludeLeasing=true&page={page_number}"
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class": AD_TYPE.CONST_PLUS_AD_TYPE()})
    return containers


def get_str_array_brands():
    url = "https://api.bilbasen.dk/metadata/makes/car?Category=bil&apikey=B3BAB31C-ED9B-4E40-8C2A-8C6627C1C685"
    uClient = uReq(url)
    xml = uClient.read()
    uClient.close()

    brands = []

    parsed = parse(xml)
    dicts = parsed["Makes"]["Make"]
    for di in dicts:
        #print(di["Name"])
        brands.append(di["Name"])

    return brands

    #brands_json = json.dumps(parsed, ensure_ascii=False)

    #test = json.loads(brands_json)
    # print(test["Makes"])

    #file = codecs.open("brands.json", "w+", "utf-8")
    #file.write(brands_json)





