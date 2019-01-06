from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    cats = requests.get("https://api.chucknorris.io/jokes/categories")
    jCats = cats.json()
    lista = " "
    for cat in jCats:
        lista = lista + " | " + cat


    return lista


if __name__ == '__main__':
    app.run(debug=True)
