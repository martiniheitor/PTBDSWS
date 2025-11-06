from flask import Blueprint

main = Blueprint('main', __name__)

from app.main.routes import main as main_blueprint
