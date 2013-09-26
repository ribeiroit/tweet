# coding: utf-8
# 
# Starts new app and config mongodb connection
#
import os
# /User/tribeiro/projetos/dojo/tweet/templates
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

from flask import Flask
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask.ext.login import LoginManager

app = Flask(__name__, static_folder='static', template_folder=tmpl_dir)
app.config.from_pyfile('config.py')
app.debug = True
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from tweet import views