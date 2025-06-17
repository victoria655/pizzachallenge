from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

db=SQLAlchemy()


  #the table creates  the many-to-many relationship between restaurants and pizzas
restaurant_pizza=db.Table('restaurant_pizza',db.metadata,
    db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurants.id'), primary_key=True),
    db.Column('pizza_id', db.Integer, db.ForeignKey('pizzas.id'), primary_key=True)
)

   


class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)

    pizzas = db.relationship('Pizza', secondary='restaurant_pizza', back_populates='restaurants',cascade='all')


    serialize_rules = {
       '-pizzas.restaurants', }
   

    def __repr__(self):
        return f'<Restaurant {self.name} {self.address}>'
    
# This is the Pizza model which represents the pizzas available in the restaurants
class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)
 
    restaurants = db.relationship('Restaurant', secondary='restaurant_pizza',back_populates='pizzas', cascade='all')

    serialize_rules = {
        '-restaurants.pizzas', 
    }   
    def __repr__(self):
        return f'<Pizza {self.name} {self.ingredients} >'
    

   
    

    