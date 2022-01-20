import os
from flask import Flask
# from config import app_config
# I need to tell Flask to read it and apply it. 
# That can be done right after the Flask application 
# instance is created using the
#  app.config.from_object() method:
app = Flask(__name__, template_folder="../templates")

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', default='dvasuygasVOIUB')
# app.config.from_object(app_config["development"])
#
from app.views import views
