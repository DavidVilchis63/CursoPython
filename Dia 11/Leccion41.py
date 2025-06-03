"""
    Ejercicio de web scraping
"""

import bs4
import requests

urlBase = "https://books.toscrape.com/catalogue/page-{}.html"

resultado = requests.get(urlBase.format("1"))
sopa = bs4.BeautifulSoup(resultado.text, "lxml")

print(len(sopa.select(".product_pod")))

