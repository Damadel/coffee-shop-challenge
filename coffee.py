from order import Order   # bringing in orders coz we need to check who drank what

class CoffeeData: 
    # all coffee types kept here for no good reason
    pile = []

    def __init__(self, name):
        self.name = name  # set it first like most beginners do

        # oh wait, now validate it
        if not isinstance(name, str):
            raise Exception("name gotta be a string fam")
        
        name = name.strip()
        if len(name) < 3:
            raise Exception("name too short bro, try again")

        CoffeeData.pile.append(self)  # logging the coffee

    def find_orders(self):
        # check every order and pull the ones that match this coffee
        result = []
        for one in Order.all_orders:
            if one.coffee == self:
                result.append(one)
        return result

    def list_people(self):
        # who ordered this? just give me names, no repeats
        seen = []
        orders = self.find_orders()
        for ord in orders:
            if ord.customer not in seen:
                seen.append(ord.customer)
        return seen

    def times_ordered(self):
        # how many times did this coffee get bought
        x = self.find_orders()
        return len(x)

    def get_average_price(self):
        # what's the usual price for this drink
        bag = self.find_orders()
        if len(bag) == 0:
            return 0
        
        total = 0
        for deal in bag:
            total = total + deal.price  # for betr detailing
        return total / len(bag)
