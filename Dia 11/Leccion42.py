"""
    Ejercicio de web scraping, segunda parte
"""

import bs4
import requests

#Crear URL sin numero de pagina
urlBase = "https://books.toscrape.com/catalogue/page-{}.html"

#Lista de titulos con 4 estrellas o mas
titulosRatingAlto = []

#Iterar pagina

for pagina in range(1, 51):

    #Crear sopa en cada pagina
    urlPagina = urlBase.format(pagina)
    resultado = requests.get(urlPagina)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")
    
    #Seleccionar datos de libros
    libros = sopa.select(".product_pod")

    #Iterar libros
    for libro in libros:

        #Revisar que tengan 4 o 5 estrellas
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:
            
            #Guardar titulo en variable
            tituloLibro = libro.select("a")[1]["title"]

            #Agregar el libro a la lista
            titulosRatingAlto.append(tituloLibro)

#Ver los libros
for t in titulosRatingAlto:
    print(t)