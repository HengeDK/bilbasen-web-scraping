from bilbasen_scraping import extract_car_info, extract_all_brands
import sys
import database as db
from bilbasen_soup import get_str_array_brands


def setup(max_pages):
    db.create_car_brand_table()
    car_brands_str_array = get_str_array_brands()
    extract_all_brands(car_brands_str_array)




def main():
    if len(sys.argv) == 1:
        setup(0)
    else:
        setup(sys.argv[1])


if __name__ == '__main__':
    main()





