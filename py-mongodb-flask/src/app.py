from flask import Flask
from Flask_Pymongo import Pymongo

app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug = True)
