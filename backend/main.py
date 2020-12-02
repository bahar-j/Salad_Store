from flask import Flask
from database import  Base, engine, DB_URL
from flask_restful import Resource, Api
import models
from models import db
from flask_cors import CORS
from werkzeug.utils import secure_filename
<<<<<<< HEAD
from all import All
from category import Category
from option import Option
from menu import Menu
<<<<<<< HEAD
from link import Link
=======

from API.all import All
from API.category import Category
from API.option import Option
from API.menu import Menu
from API.order import Order
from API.statistic import Statistic
>>>>>>> 759bd985697a408ce0f49bd677dc8c00f75e381c
=======
from order import Order
from link import Link
from statistic import Statistic
>>>>>>> 8f4724707cc91e41531f459296d448f116fce0c4

Base.metadata.create_all(bind=engine)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    models.db.init_app(app)
    CORS(app, resources={r'*': {'origins': '*'}})

    return app

app = create_app()
api = Api(app)
app.secret_key = "super secret key"

api.add_resource(Order, '/orders')
api.add_resource(Statistic, '/statistics')
api.add_resource(All,'/all')
api.add_resource(Option,'/option')
api.add_resource(Category,'/category')
api.add_resource(Menu, '/menu')
api.add_resource(Link, '/link')

if __name__=='__main__':
    app.run(debug=True)

