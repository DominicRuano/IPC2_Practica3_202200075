from pelicula import Pelicula

peliculas = []


def addPelicula(id, nombre, genero):
    peliculas.append(Pelicula(id, nombre, genero))

def filtrogenero(genero):
    dic = []
    for pelicula in peliculas:
        if pelicula.Genero == genero:
            dic.append({"Nombre": pelicula.Nombre, "Genero": pelicula.Genero, "movieId": pelicula.IdPelicula})
    return dic