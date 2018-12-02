from bilbasen_scraping import extract_car_info, extract_car_brands_and_fill_table, get_count_of_pages
import sys
import database as db


def setup(max_pages):
    db.create_car_brand_table()
    extract_car_brands_and_fill_table()

    get_count_of_pages()


def main():
    if len(sys.argv) == 1:
        setup(0)
    else:
        setup(sys.argv[1])


if __name__ == '__main__':
    main()





