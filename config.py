import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname((__file__)))

connex_app = connexion.App(__name__, specificaiton_dir=basedir)

app = connext_app.app

sqlite_url = 'sqlite:////' + os.path.join(basedir, 'people.db')

app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)