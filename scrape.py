from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import constants.listing_types as AD_TYPE
from bilbasen_scraping import extract_car_info



# URL to scrape
bmw_url = "https://www.bilbasen.dk/brugt/bil/bmw"

# Open a HTTP request to the URL, and load the response into a variable
uClient = uReq(bmw_url)
# Read the HTML response returned into a variable
page_html = uClient.read()
# Close the request after reading
uClient.close()

# Parse the HTML using bs4
page_soup = soup(page_html, "html.parser")

# Grab the divs containing the cars, currently only 1 page, and currently only the 'plus' listing type
containers = page_soup.findAll("div", {"class": AD_TYPE.CONST_PLUS_AD_TYPE()})

extract_car_info(containers)







