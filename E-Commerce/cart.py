class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class Cart:
    def __init__(self):
        self.items = []

    def add(self, product, quantity):
        if quantity > product.quantity:
            raise ValueError("Quantity exceeds stock.")
        self.items.append(CartItem(product, quantity))

    def is_empty(self):
        return len(self.items) == 0