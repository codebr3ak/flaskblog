from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f80930995d450ff7107857a3aff66b65'
app.config['SQLALCHEMY_ DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flaskblog import routes