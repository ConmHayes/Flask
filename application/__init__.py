from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://krauphyg:W4i0jWkLYTYyzcD0huWmRifJ2GglXJWH@trumpet.db.elephantsql.com/krauphyg'
db = SQLAlchemy(app)

from application import routes