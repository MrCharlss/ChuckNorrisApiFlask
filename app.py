from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    cats = requests.get("https://api.chucknorris.io/jokes/categories")
    jCats = cats.json()
    for cat in jCats:
        print(cat)

    return jCats[2]


if __name__ == '__main__':
    app.run(debug=True)
