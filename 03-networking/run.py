import mysql.connector
import json
from flask import Flask
import requests

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Hello World"


@app.route("/movies", methods=["GET"])
def get_movies():
    try:
        response = requests.get("https://swapi.dev/api/films")

        return json.loads(response.content.decode())

    except Exception as e:
        print(e)


@app.route("/people", methods=["GET"])
def get_people():
    try:
        response = requests.get("https://swapi.dev/api/people")

        return json.loads(response.content.decode())

    except Exception as e:
        print(e)


@app.route("/db", methods=["GET"])
def get_db():
    try:
        cnx = mysql.connector.connect(
            user="root", database="movies", password="root", host="mysql_db"
        )

        with cnx.cursor() as cursor:

            result = cursor.execute("SELECT * FROM favorite")

            rows = [
                dict(zip(["id", "gender", "movie", "url"], row))
                for row in cursor.fetchall()
            ]

            return {"data": rows}

    except Exception as err:
        return {"error": str(err)}


# Usar app.run(host="0.0.0.0") em Flask quando se roda dentro de um contêiner Docker é uma prática comum. Isso configura o Flask para escutar em todas as interfaces de rede disponíveis no contêiner Docker. O endereço IP 0.0.0.0 significa "qualquer endereço disponível".

app.run(debug=True, port=5000, host="0.0.0.0")
