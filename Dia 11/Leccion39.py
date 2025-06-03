"""
    Programar un extractor de datos o web scraping
"""


import bs4
import requests

#Buscar variable con requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html")
print(type(resultado))
#print(resultado.text)

#Metodos de BS4

sopa = bs4.BeautifulSoup(resultado.text, "lxml")
#print(sopa)
print(sopa.select("title"))
print(len(sopa.select("p")))
print(sopa.select("title")[0].getText())