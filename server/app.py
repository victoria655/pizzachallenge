from flask import Flask, jsonify, make_response,request
from flask_migrate import Migrate
from models import db, Restaurant, Pizza,RestaurantPizza
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config.from_prefixed_env()


db.init_app(app)
migrate = Migrate(app, db)

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    response = []

    for restaurant in restaurants:
        response.append(restaurant.to_dict())
    if not response:
        return make_response(jsonify(response), 204) 
    else:
        return make_response(jsonify(response), 200)
        
@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get_or_404(id)
    return restaurant.to_dict()

@app.route('/restaurants', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get_or_404(id)
    db.session.delete(restaurant)
    db.session.commit()
    return make_response(jsonify({'message': 'Restaurant deleted successfully'}), 204)
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    response = []

    for pizza in pizzas:
        response.append(pizza.to_dict())
    if not response:
        return make_response(jsonify(response), 204) 
    else:
        return make_response(jsonify(response), 200)
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    # Validation
    if price is None or not (1 <= price <= 30):
        return make_response(jsonify({"errors": ["Price must be between 1 and 30"]}), 400)

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    if not pizza or not restaurant:
        return make_response(jsonify({"error": "Pizza or Restaurant not found"}), 404)

    # ✅ Use the RestaurantPizza model
    new_rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(new_rp)
    db.session.commit()

    response_data = {
        "id": new_rp.id,
        "price": new_rp.price,
        "pizza_id": new_rp.pizza_id,
        "restaurant_id": new_rp.restaurant_id,
        "pizza": {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        },
        "restaurant": {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        }
    }

    return make_response(jsonify(response_data), 201)
