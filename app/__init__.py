from flask import Flask
import os

app = Flask(__name__)

if not os.getenv('KC_ENV'):
    os.environ['KC_ENV'] = "config.Development"

app.config.from_object(os.environ['KC_ENV'])

from app.controllers import home_controller
