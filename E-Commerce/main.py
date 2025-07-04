from datetime import date, timedelta
from cart import Cart
from customer import Customer
from checkout import checkout
from product import Cheese, TV, ScratchCard, Biscuits

cheese = Cheese(price=100, quantity=5, expiry_date=date.today() + timedelta(days=5), weight=200)
tv = TV(price=300, quantity=3, weight=10000)
scratch_card = ScratchCard(price=50, quantity=10)
biscuits = Biscuits(price=150, quantity=2, expiry_date=date.today() + timedelta(days=1), weight=700)

customer = Customer("Ali", balance=500)

cart = Cart()
cart.add(cheese, 2)
cart.add(biscuits, 1)
cart.add(scratch_card, 1)

checkout(customer, cart)