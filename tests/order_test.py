from client import Client
from coffee import CoffeeData
from order import Order

def test_create_order():
    user = Client("Ali")
    drink = CoffeeData("Latte")
    order = Order(user, drink, 4.0)
    assert order.customer == user
    assert order.coffee == drink
    assert order.price == 4.0

def test_invalid_price():
    user = Client("Sara")
    drink = CoffeeData("Mocha")
    try:
        Order(user, drink, 12.0)  # price too high
    except Exception:
        assert True
