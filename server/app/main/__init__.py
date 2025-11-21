#Defines blueprint
from flask import Blueprint

main_bp = Blueprint('main', __name__)

from . import routes  # Import routes here to register them with the blueprint

