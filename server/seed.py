from app import app
from models import db, Pizza, Restaurant, RestaurantPizza

with app.app_context():
    # 1. Delete all data from child tables first (due to foreign key constraints)
    db.session.query(RestaurantPizza).delete()
    db.session.query(Pizza).delete()
    db.session.query(Restaurant).delete()

    # 2. Commit the deletions
    db.session.commit()

    # 3. Create new pizzas
    pizza1 = Pizza(name='Margherita', ingredients='Tomato, Mozzarella, Basil')
    pizza2 = Pizza(name='Pepperoni', ingredients='Tomato, Mozzarella, Pepperoni')
    pizza3 = Pizza(name='Vegetarian', ingredients='Tomato, Mozzarella, Bell Peppers, Olives')

    # 4. Create new restaurants
    restaurant1 = Restaurant(name='Pizza Palace', address='123 Pizza St')
    restaurant2 = Restaurant(name='Pasta Place', address='456 Pasta Ave')
    restaurant3 = Restaurant(name='Burger Bistro', address='789 Burger Blvd')

    # 5. Add pizzas and restaurants
    db.session.add_all([pizza1, pizza2, pizza3, restaurant1, restaurant2, restaurant3])
    db.session.commit()

    # 6. Create new RestaurantPizza entries
    rp1 = RestaurantPizza(restaurant_id=restaurant1.id, pizza_id=pizza1.id, price=10.99)
    rp2 = RestaurantPizza(restaurant_id=restaurant2.id, pizza_id=pizza2.id, price=12.49)
    rp3 = RestaurantPizza(restaurant_id=restaurant3.id, pizza_id=pizza3.id, price=9.99)

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()

    print("✅ Database cleared and re-seeded successfully!")
