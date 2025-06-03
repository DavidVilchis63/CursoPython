"""
    Extraer imagenes con bs4 y requests
"""


import bs4
import requests

resultado = requests.get("https://escueladirecta.com/courses")
sopa = bs4.BeautifulSoup(resultado.text, "lxml")

imagenes = sopa.select(".ProductImage")[0]["src"]
print(imagenes)

imagenCurso1 = requests.get(imagenes)
#print(imagenCurso1.content)

f = open("miImagen.jpg", "wb")
f.write(imagenCurso1.content)
f.close()

