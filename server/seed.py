from app import app
from models import db, Pizza, Restaurant, restaurant_pizza

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create pizzas
    pizza1 = Pizza(name='Margherita', ingredients='Tomato, Mozzarella, Basil')
    pizza2 = Pizza(name='Pepperoni', ingredients='Tomato, Mozzarella, Pepperoni')
    pizza3 = Pizza(name='Vegetarian', ingredients='Tomato, Mozzarella, Bell Peppers, Olives')

    # Create restaurants
    restaurant1 = Restaurant(name='Pizza Palace', address='123 Pizza St')
    restaurant2 = Restaurant(name='Pasta Place', address='456 Pasta Ave')
    restaurant3 = Restaurant(name='Burger Bistro', address='789 Burger Blvd')

    # Associate pizzas with restaurants
    restaurant1.pizzas.append(pizza1)
    restaurant2.pizzas.append(pizza2)
    restaurant3.pizzas.append(pizza3)

    # Add to session and commit
    db.session.add_all([restaurant1, restaurant2, restaurant3])
    db.session.commit()

    print("Database added successfully!")