import csv
import os

curr_dir = os.getcwd()
path = '/Users/alif/Documents/code/Python_OOP/Store Manager/items.csv'

class Item:

    whole_list = []

    #Constructor 
    def __init__(self, name: str, __price: float, quantity = 0):

        #Raise flags for correct inputs
        assert __price >= 0, f"Price {self.__price} is not greater than $0"
        assert quantity > 0, f"Quantity {self.quantity} is not greater than $0"

        #Add attributes
        self.__name = name
        self.__price = __price
        self.quantity = quantity

        #Adding to list
        Item.whole_list.append(self)

    #Changing name to read only using property decorator
    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    #Get the discounted __price given item, pass global scope if not entered manually
    discount_rate = 0.8
    def discount_price(self):
        return self.__price * self.discount_rate

    def increment_price(self, increment_rate):
        self.__price=  self.__price + (self.__price * increment_rate)

    #Allow new way to change name 
    @name.setter
    def name(self, value):
        if len(value)>10:
            raise Exception ("Name is too long")
        else:
            self.__name = value

    #Print total expected revenue
    def get_total(self):
        return self.quantity * self.__price


    #Dictionary / String representation
    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", {self.__price}, {self.quantity})'

    #Read csv instead of having us pass in each item
    @classmethod
    def read_from_csv(cls):
        #with open(path, 'r') as f:
        with open(f'{curr_dir}/Store Manager/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                __price = float(item.get('__price')),
                quantity = int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        #We will ignore floats ie 5.0, 10.0
        if isinstance(num, float):
            #Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
             return False