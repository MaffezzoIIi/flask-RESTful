from flask import Flask
from db.banco import Banco

Banco()


def create_app():
    return Flask(__name__)


app = create_app()


@app.route('/')
def index():
    return 'Hello, World!'
