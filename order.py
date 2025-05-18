# tracking all the drinks people buy

class Order:
    # all orders go in here. just dumping them for now
    all_orders = []

    def __init__(self, buyer, drink, amount):
        self.customer = buyer
        self.coffee = drink
        self.price = amount

        # not gonna lie, let's rn sm checks here

        # did we even pass a proper person?
        if not hasattr(buyer, 'name'):
            raise Exception("uhh 'buyer' needs to be like... a person? with a name?")

        # same for coffee
        if not hasattr(drink, 'name'):
            raise Exception("not a valid drink. make it a coffee obj maybe")

        # make sure price is a float
        if not isinstance(amount,float):
            raise Exception("float only bro. use 3.0 or 2.5 not just 3")

        # range check
        if amount < 1.0 or amount > 10.0:
            raise Exception("yo price gotta be between 1.0 and 10.0 — that’s the rule")

        # slap it into the list
        Order.all_orders.append(self)