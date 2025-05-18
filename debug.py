from client import Client

from coffee import CoffeeData

from order import Order



# making a few fake people

a = Client("abdullahi")

b = Client("Gloria")

c = Client("Mathew")

d = Client("Lily")



# some coffee stuff

latte = CoffeeData("Latte")

mocha = CoffeeData("Mocha")

espresso = CoffeeData("Espresso")

chai = CoffeeData("Chai")

# orders incoming 

o1 = Order(a, latte, 3.5)

o2 = Order(a, mocha, 4.0)

o3 = Order(b, latte, 4.5)

o4 = Order(c, espresso, 2.5)

o5 = Order(a, espresso, 3.0)

o6 = Order(d, chai, 3.5)



# just checking stuff, not fancy

print("Orders for Latte:")

for order in latte.find_orders():

  print(f"- {order.customer.name} paid {order.price}")



print("\nWho drank Espresso?")

for person in espresso.list_people():

  print("-", person.name)



print("\nHow many times was Mocha ordered?")

print(mocha.times_ordered())

print("\nWho drank Chai?")
for person in chai.list_people():
    print("-", person.name)

print("\nHow many times was Chai ordered?")
print(chai.times_ordered())

print("\nTop spender on Latte:")
top = Client.spender_alert(latte)

if top:
    print(top.name)
else:
    print("No one bought this yet ")

print("\nTop spender on chai:")
top = Client.spender_alert(chai)

if top:
    print(top.name)
else:
    print("No one bought this yet ")