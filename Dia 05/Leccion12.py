# Tuplas en funciones y ejemplos de uso

precios_cafe = [("Americano", 2.5), ("Latte", 3.0), ("Mocha", 3.5), ("Capuccino", 3.58), ("Expresso", 2.0)];

for cafe,precio in precios_cafe:
    print(cafe)

def cafe_mas_caro(precios_cafes):

    cafe_mas_caro = "";
    precio_cafe_mas_caro = 0;

    for cafe,precio in precios_cafes:
        if precio > precio_cafe_mas_caro:
            cafe_mas_caro = cafe;
            precio_cafe_mas_caro = precio;
        else:
            pass

    return cafe_mas_caro, precio_cafe_mas_caro;

print(cafe_mas_caro(precios_cafe))