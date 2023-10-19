from flask import request, jsonify, Flask
from flask_cors import CORS
from Functions import addPelicula

app = Flask(__name__)
CORS(app)

@app.route('/api/new-movie', methods = ["POST"]) #por defecto es de tipo GET
def postHome():
    try:
        idFilm = request.json["movieId"]
        nombre= request.json["name"]
        genre = request.json["genre"]
        genre = genre.lower()
        if idFilm and nombre and genre:
            addPelicula(idFilm, nombre, genre)
            return jsonify({"message": "datos leidos correctamente"})
        else:
            return jsonify({"message": "Ocurrio un error inesperado al leer json"})
    except:
        return jsonify({"message": "Ocurrio un error, verifique el json"})

@app.route("/", methods = ["GET"])
def getHome():
    return jsonify({"message": "ipc2 desde un get ahora mismo"})


if __name__ == '__main__':
    app.run(debug=True, port=3000)