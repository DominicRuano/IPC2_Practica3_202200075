
class Pelicula():
    def __init__(self, Id, nombre, genero) -> None:
        self.IdPelicula = Id
        self.Nombre = nombre
        self.genero = genero
    
    def imprimirPelicula(self):
        print(f"----------\nNombre: {self.Nombre} \nGenero: {self.genero} \nID: {self.IdPelicula}")
    
    def getDatos(self):
        return self.IdPelicula, self.Nombre, self.genero