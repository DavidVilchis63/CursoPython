# Calculador de comisisones

nombre = input("Escribe tu nombre: ");
ventas = input("Cuanto vendiste: ");

ventas = float(ventas);
ganancia = (ventas * 0.13) + ventas
print(f"{nombre}, este periodo ganaste un total de {round(ganancia,2)}, por tus ventas, por tu comision de {ganancia-ventas}")