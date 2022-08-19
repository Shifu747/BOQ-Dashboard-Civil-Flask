from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app =Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///boqDB.db'
app.config['SECRET_KEY'] = 'afnjlanklfjajhsfjlasjlhfjlashjlfja3i9022'

db = SQLAlchemy(app)

from application import routes