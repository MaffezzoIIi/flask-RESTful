from flask import Flask
from db.banco import Banco

def create_app():
    return Flask(__name__)

def create_db():
    Banco()

create_db()
app = create_app()

@app.route('/')
def index():
    return 'Hello, World!'
    