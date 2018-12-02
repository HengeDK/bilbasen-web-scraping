import pyodbc
from pandas import read_sql_query

def CONST_DB_SERVER():
    return "localhost"


def CONST_DB_NAME():
    return "bilbasendb"


def CONST_DB_USERNAME():
    return "virtus"


def CONST_DB_PASSWORD():
    return "password"


def get_db_connection():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + CONST_DB_SERVER() + ';DATABASE=' + CONST_DB_NAME() + ';UID=' + CONST_DB_USERNAME() + ';PWD=' + CONST_DB_PASSWORD())
    return conn


def insert_brand(brand_str):
    conn = get_db_connection()
    sql = f"INSERT INTO Brands(brand) VALUES('{brand_str}')"
    conn.cursor().execute(sql)
    conn.commit()


def get_car_brands():
    conn = get_db_connection()
    query = "SELECT * FROM Brands"
    result = read_sql_query(query, conn)
    all_brands = result.Brand
    return all_brands


def table_exists(table):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE '" + table + "'"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False


def delete_table(table):
    conn = get_db_connection()
    if table_exists(table):
        sql = "DROP TABLE " + table
        conn.cursor().execute(sql)
        conn.commit()


def create_car_brand_table():
    conn = get_db_connection()
    if table_exists('Brands'):
        delete_table('Brands')

    conn.cursor().execute("CREATE TABLE Brands(Brand CHAR(100))")
    conn.commit()

