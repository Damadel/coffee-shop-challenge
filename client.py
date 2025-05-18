# grabbing from the Order class so we can use it below
from order import Order

class Client:
    # this holds every person that orders something
    people_log = []

    def __init__(self, username):
        # quick name check - don't want gibberish
        if isinstance(username, str) and 1 <= len(username.strip()) <= 15:
            self.name = username
        else:
            raise Exception("invalid name - must be 1-15 characters and a string")

        # save this person for later checks
        Client.people_log.append(self)

    def fetch_orders(self):
        # look thru every order and filter the ones by this client
        my_orders = []
        for each in Order.all_orders:
            if each.customer == self:
                my_orders.append(each)
        return my_orders

    def what_coffees(self):
        # returns all dif coffee types the person ordered
        kinds = set()
        for o in self.fetch_orders():
            kinds.add(o.coffee)
        return list(kinds)

    def make_order(self, which_coffee, how_much):
        # places an order and returns the order object
        return Order(self, which_coffee, how_much)

    @classmethod
    def spender_alert(cls, coffee_type):
        # go through each client and find who spent the most
        highest = 0
        champ = None
        for guy in cls.people_log:
            spent = 0
            for buy in guy.fetch_orders():
                if buy.coffee == coffee_type:
                    spent += buy.price
            if spent > highest:
                highest = spent
                champ = guy
        return champ