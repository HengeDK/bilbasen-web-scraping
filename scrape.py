from bilbasen_scraping import extract_car_brands_and_fill_table
import sys
import database as db
from bilbasen_scraping import start_scraping_cars


def setup(max_pages):
    db.create_car_brand_table()
    extract_car_brands_and_fill_table()

    db.create_cars_table()

    start_scraping_cars(max_pages)


def main():
    if len(sys.argv) == 1:
        setup(0)
    else:
        setup(sys.argv[1])


if __name__ == '__main__':
    main()





