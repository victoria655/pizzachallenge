from flask import Flask, jsonify, make_response,request
from flask_migrate import Migrate
from models import db, Restaurant, Pizza
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
@app.route('/pizzas', methods=['POST'])
def create_pizza():
    data = request.get_json()
    new_pizza = Pizza(name=data['name'], ingredients=data['ingredients'])
    db.session.add(new_pizza)
    db.session.commit()
    return make_response(jsonify(new_pizza.to_dict()), 201)