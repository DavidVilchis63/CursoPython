"""
    Ejercicio de web scraping
"""

import bs4
import requests

urlBase = "https://books.toscrape.com/catalogue/page-{}.html"

for n in range(1,11):
    print(urlBase.format(n))
