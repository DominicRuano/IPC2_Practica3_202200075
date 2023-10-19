from pelicula import Pelicula

peliculas = []


def addPelicula(id, nombre, genero):
    peliculas.append(Pelicula(id, nombre, genero))

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