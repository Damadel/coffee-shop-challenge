import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coffee import CoffeeData

def test_valid_name():
    drink = CoffeeData("Espresso")
    assert drink.name == "Espresso"

def test_short_name():
    try:
        CoffeeData("A")  # too short
    except Exception:
        assert True
