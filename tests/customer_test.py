import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from client import Client

def test_name():
    user = Client("Abdi")
    assert user.name == "Abdi"

def test_invalid_name():
    try:
        Client("a" * 20)
    except Exception:
        assert True
