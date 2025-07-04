from datetime import date
from abc import ABC, abstractmethod

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def is_expired(self):
        return False

    def is_shippable(self):
        return False

class Expirable(Product):
    def __init__(self, name, price, quantity, expiry_date: date):
        super().__init__(name, price, quantity)
        self.expiry_date = expiry_date

    def is_expired(self):
        return date.today() > self.expiry_date

class Shippable(Product, ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_weight(self):
        pass

    def is_shippable(self):
        return True

class Cheese(Expirable, Shippable):
    def __init__(self, price, quantity, expiry_date, weight):
        Expirable.__init__(self, "Cheese", price, quantity, expiry_date)
        self.weight = weight

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

class Biscuits(Expirable, Shippable):
    def __init__(self, price, quantity, expiry_date, weight):
        Expirable.__init__(self, "Biscuits", price, quantity, expiry_date)
        self.weight = weight

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

class TV(Shippable):
    def __init__(self, price, quantity, weight):
        super().__init__("TV", price, quantity)
        self.weight = weight

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

class ScratchCard(Product):
    def __init__(self, price, quantity):
        super().__init__("ScratchCard", price, quantity)