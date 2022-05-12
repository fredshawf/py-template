from flask import Flask
from .boot import Boot
import os

root_path = os.path.abspath('.')
Flask.app = app = Flask(__name__, root_path = root_path)
Flask.app.env = os.environ['FLASK_ENV'] if ('FLASK_ENV' in os.environ) else 'development'
Flask.app.root = root_path

Boot.start()