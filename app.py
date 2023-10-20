from flask import request, jsonify, Flask
from flask_cors import CORS
from Functions import addPelicula, filtrogenero, getTodo, actualizar

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ["GET"])
def getHome():
    return jsonify({"message": "API esta viva!"})

@app.route("/api/get-todo", methods = ["GET"])
def gettodo():
    return getTodo()

@app.route('/api/new-movie', methods = ["POST"]) #por defecto es de tipo GET
def postAddMovie():
    try:
        idFilm = request.json["movieId"]
        nombre= request.json["name"]
        genre = request.json["genre"]
        genre = genre.lower()

        valor = addPelicula(idFilm, nombre, genre)
        if valor == 1:
            return jsonify({"message": "datos leidos correctamente."})
        if valor == 2:
            return jsonify({"message": "no se pueden agregar dos peliculas con el mismo id."})
    except:
        return jsonify({"message": "Ocurrio un error, verifique el json."})

@app.route("/api/all-movies-by-genre/<genero>", methods = ["GET"])
def getFiltroGenero(genero):
    return filtrogenero(genero.lower())

@app.route("/api/update-movie", methods = ["PUT"])
def putActualizar():
    try:
        idFilm = request.json["movieId"]
        nombre= request.json["name"]
        genre = request.json["genre"].lower()

        if actualizar(idFilm, nombre, genre):
            return jsonify({"message": "datos Actualizados correctamente."})
        else:
            return jsonify({"message": "No se puedo enconntrar una pelicula para actualizar."})
    except:
        return jsonify({"message": "Ocurrio un error, verifique el json."})

if __name__ == '__main__':
    app.run(debug=True, port=3000)