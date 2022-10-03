import os
from flask import Flask

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


def create_application():
    app = Flask(__name__)

    return app





