from flask import Blueprint, jsonify, abort
from ..models.restaurant import Restaurant
from ..models import db

restaurant_bp = Blueprint('restaurant_bp', __name__, url_prefix='/restaurants')

@restaurant_bp.route('/', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([r.to_dict() for r in restaurants]), 200
