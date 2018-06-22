from flask import Flask
from flask_frozen import Freezer
from flask_flatpages import FlatPages


app = Flask(__name__)
app.config.from_pyfile('settings.py')
pages = FlatPages(app)
freezer = Freezer(app)


from .views import *
