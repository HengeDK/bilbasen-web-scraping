def format_kml_str(str_to_format):
    return str_to_format.replace("km/l", "").replace(",", ".").replace("-", "")


def format_kmt_str(str_to_format):
    return str_to_format.replace("sek.", "").replace(",", ".").replace("-", "")


def format_price_str(str_to_format):
    return int(str_to_format.replace("kr.", "").replace(".", "").replace("Ring", "0"))
