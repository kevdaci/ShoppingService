from flask import Flask
from src.controller.order import order

def create_app():
	app = Flask(__name__)
	app.register_blueprint(order)
	return app

