from pelicula import Pelicula

peliculas = []


def addPelicula(id, nombre, genero):

    for pelicula in peliculas:
        if pelicula.IdPelicula == id:
            return 2

    peliculas.append(Pelicula(id, nombre, genero))
    return 1

def getTodo():
    dic = []
    for pelicula in peliculas:
        dic.append({"Nombre": pelicula.Nombre, "Genero": pelicula.Genero, "movieId": pelicula.IdPelicula})
    return dic

def filtrogenero(genero):
    dic = []
    for pelicula in peliculas:
        if pelicula.Genero == genero:
            dic.append({"Nombre": pelicula.Nombre, "Genero": pelicula.Genero, "movieId": pelicula.IdPelicula})
    return dic

def actualizar(id, nombre, genero):
    for pelicula in peliculas:
        if pelicula.IdPelicula == id:
            pelicula.Nombre = nombre
            pelicula.Genero = genero
            return True