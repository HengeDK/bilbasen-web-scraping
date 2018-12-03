# bilbasen-web-scraping
Bilbasen.dk web scraping, Python 3.7

1) `pip install -r requirements.txt`
2) Installer `Microsoft ODBC Driver 17 for SQL Server`: https://www.microsoft.com/en-us/download/details.aspx?id=56567
3) Opret database `bilbasendb` på MSSQL
4) Opret login på `bilbasendb`, ændre server, username og password i `constants/db_conf.py`
5) Kør scrape.py: `$ python scrape.py <page_limit>`
6) Alle sider: `$ python scrape.py`

`page_limit` = Maks antal sider der skal gemmes. 1 side = 32 biler. Som regel 1600 sider i alt.
