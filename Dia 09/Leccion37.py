"""
    Modulo RE expresiones regulares

[ ] un set de caracteres
.   un carácter cualquiera
^   inicia con
$   finaliza con
*   cero o más ocurrencias
+   una o más ocurrencias
{ } un número especificado de ocurrencias
?   cero o una ocurrencia
|   operador lógico "O"
\d  dígito numérico
\D  NO numérico
\w  caracter alfanumérico
\W  NO alfanumérico
\s  espacio en blanco
\S  NO espacio en blanco
"""

import re

texto = "Aprender un poco cada día marca la diferencia. Hay estudios que muestran que los estudiantes que hacen del aprendizaje un hábito tienen una mayor probabilidad de alcanzar sus objetivos. Reserva tiempo para aprender y recibe recordatorios con la herramienta de planificación del aprendizaje."
patron = "la"


busqueda = re.search(patron, texto)
print(busqueda)
print(busqueda.span())
print(busqueda.start())
print(busqueda.end())

print("*" * 20)
busqueda = re.findall(patron, texto)
print(busqueda)
print(len(busqueda))

print("*" * 20)
for encontrada in re.finditer(patron, texto):
    print(encontrada.span())

print("*" * 20)
texto2 = "lamma al 565-568-2469 para...."
patron2 = re.compile(r"(\d{3})-(\d{3})-(\d{4})" )             #r"\d\d\d-\d\d\d-\d\d\d\d"
resultado2 = re.search(patron2, texto2)
print(resultado2)
print(resultado2.group())
print(resultado2.group(2))