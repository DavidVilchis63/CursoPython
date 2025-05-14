# Metodos especiales

class Disco:

    def __init__(self, autor, titulo, canciones):

        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    #Define que mostrara cuando alguien pida imprimir metodo print()
    def __str__(self):
        return f"Albun: {self.titulo} de {self.autor}"

    # Define como se comportara cuando alguien pida el metodo len()
    def __len__(self):
        return self.canciones

    # Define como se comportara cuando alguien pida el metodo del()
    def __del__(self):
        print("Se ha eliminado el cd")

miCd = Disco("Pink Floyd", "The Wall", 24)

print(miCd)
print(len(miCd))

#Metodo para eliminar instancias
del miCd