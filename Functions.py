from pelicula import Pelicula

peliculas = []


def addPelicula(id, nombre, genero):
    peliculas.append(Pelicula(id, nombre, genero))
    
    for pelicula in peliculas:
        pelicula.imprimirPelicula()
        pass