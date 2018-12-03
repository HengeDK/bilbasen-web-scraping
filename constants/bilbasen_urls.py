def CONST_BASE_URL():
    return "https://www.bilbasen.dk"


def CONST_BASE_API_URL():
    return "https://api.bilbasen.dk"


def CONST_CAR_BRANDS_URL():
    return CONST_BASE_API_URL() + "/metadata/makes/car?Category=bil&apikey=B3BAB31C-ED9B-4E40-8C2A-8C6627C1C685"


def CONST_CAR_LISTINGS_MAX_PAGE():
    return CONST_BASE_URL() + "/brugt/bil?Fuel=0&YearFrom=0&YearTo=0&PriceFrom=0&PriceTo=10000000&MileageFrom=-1&MileageTo=10000001&IncludeEngrosCVR=true&IncludeLeasing=true&page=99999"


def CONST_CAR_LISTINGS_VARIABLE_PAGE_NUMBER(page_num):
    return f"https://www.bilbasen.dk/brugt/bil?Fuel=0&YearFrom=0&YearTo=0&PriceFrom=0&PriceTo=10000000&MileageFrom=-1&MileageTo=10000001&IncludeEngrosCVR=true&IncludeLeasing=true&page={page_num}"
