from flask import request, jsonify, Flask
from flask_cors import CORS
from Functions import addPelicula, filtrogenero

app = Flask(__name__)
CORS(app)

@app.route('/api/new-movie', methods = ["POST"]) #por defecto es de tipo GET
def postHome():
    try:
        idFilm = request.json["movieId"]
        nombre= request.json["name"]
        genre = request.json["genre"]
        genre = genre.lower()

        addPelicula(idFilm, nombre, genre)
        return jsonify({"message": "datos leidos correctamente"})
    except:
        return jsonify({"message": "Ocurrio un error, verifique el json"})

@app.route("/api/all-movies-by-genre/<genero>", methods = ["GET"])
def getHome(genero):
    return filtrogenero(genero.lower())


if __name__ == '__main__':
    app.run(debug=True, port=3000)