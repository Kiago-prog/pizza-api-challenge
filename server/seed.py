from models import db
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurant_pizza import RestaurantPizza
from app import create_app


app = create_app()

with app.app_context():
    print("Seeding database...")

    # Clear existing data (optional for development)
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    # Create pizzas
    pizza1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    pizza2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
    pizza3 = Pizza(name="Veggie", ingredients="Tomato, Olives, Peppers, Onions")
    db.session.add_all([pizza1, pizza2, pizza3])
    db.session.commit()

    # Create restaurants
    r1 = Restaurant(name="Pizza Mojo", address="King's Road 103")
    r2 = Restaurant(name="Dominos", address="High Street 696")
    db.session.add_all([r1, r2])
    db.session.commit()

    # Link pizzas to restaurants
    rp1 = RestaurantPizza(price=10, pizza_id=pizza1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=12, pizza_id=pizza2.id, restaurant_id=r1.id)
    rp3 = RestaurantPizza(price=8, pizza_id=pizza3.id, restaurant_id=r2.id)
    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()

    print("Done seeding!")
