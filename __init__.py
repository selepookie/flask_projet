from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f65588e97c7bfd6e354ad97112a4daf4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://anonyme:admin@localhost/Site'

db = SQLAlchemy(app)

from . import routes