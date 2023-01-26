
from items import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_count=0):
        #Extend from Item class
        super().__init__(name, price, quantity)

        #Raise flags for correct inputs
        assert broken_count >= 0, f"Broken Phone {self.broken_count} is not greater than 0"

        #Attributes specific to phones
        self.broken_count = broken_count