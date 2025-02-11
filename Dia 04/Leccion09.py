# Funcion Zip

nombres = ["Ana", "Hugo", "Valeria"];
edades = [69,29,42];
ciudades = ["Lima", "Madrid", "Mexico"]

combinados = list(zip(nombres, edades,ciudades));

print(combinados)

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
    
# Funcion min y max

lista = [134,46,75,314,241,134];

print(f"El menor es {min(lista)} y el mayor es {max(lista)}");

