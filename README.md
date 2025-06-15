# Pizza Restaurant API

A RESTful Flask API for managing restaurants, pizzas, and their relationships.
This project follows the MVC pattern and uses SQLAlchemy with Flask-Migrate for ORM and database migrations.
---

##  Setup Instructions

1. **Clone the repo:**

git clone git@github.com:Alicia-Natasha/pizza-api-challenge.git
cd pizza-api-challenge

2. Install dependencies:

pipenv install flask flask_sqlalchemy flask_migrate flask-cors
pipenv shell

3. Set Flask environment:

export FLASK_APP=server.app:create_app

4. Run migrations:

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

5. Seed the database:

python server/seed.py

6. Run the server:

flask run

## Routes Summary

### Restaurants
GET /restaurants
Returns all restaurants

GET /restaurants/<id>
Returns one restaurant and its pizzas
404 if not found

DELETE /restaurants/<id>
Deletes a restaurant and associated RestaurantPizzas
204 No Content if successful
404 if not found

### Pizzas
GET /pizzas
Returns all pizzas

### RestaurantPizzas (Join Table)
POST /restaurant_pizzas
Creates a RestaurantPizza
Request body:

{
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 2
}
 On success: returns joined pizza + restaurant data
 On invalid price:

{ "errors": ["Price must be between 1 and 30"] }

## Validation Rules
RestaurantPizza.price must be between 1 and 30 (inclusive)

If any input fails validation, the API returns a 400 with error messages

## Testing with Postman
Open Postman

Import challenge-1-pizzas.postman_collection.json

Test each route (GET, POST, DELETE)

## Dependencies
Uses Flask + SQLAlchemy + Flask-Migrate

Follows MVC pattern (models/, controllers/, app.py)

Fully RESTful API — no frontend required

## Author
Alicia Natasha
---
## License
