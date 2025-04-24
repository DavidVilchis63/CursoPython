#Modulo Pathlib

from pathlib import Path

carpeta = Path("C:/Users/david/Documents/Python/Dia 06/Prueba00.txt") 

print(carpeta.read_text())      #Para este no se necesita abrir y cerrar archivo

