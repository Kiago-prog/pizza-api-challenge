from flask import Blueprint, request, jsonify
from ..models import db
from ..models.restaurant_pizza import RestaurantPizza
from ..models.pizza import Pizza
from ..models.restaurant import Restaurant
from sqlalchemy.exc import IntegrityError

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__, url_prefix='/restaurant_pizzas')

@restaurant_pizza_bp.route('/', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        new_rp = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        db.session.add(new_rp)
        db.session.commit()
        return jsonify(new_rp.to_dict()), 201
    except ValueError as ve:
        return jsonify({"errors": [str(ve)]}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"errors": ["Invalid restaurant_id or pizza_id"]}), 400
