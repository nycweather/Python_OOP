class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.density = weight / value

def knapsack(items, capacity):
    items.sort(key=lambda x: x.density, reverse=True)
    usedCapacity = 0
    total = 0
    for item in items:
        if usedCapacity + item.weight <= capacity:
            usedCapacity += item.weight
            total += item.value
        else:
            unusedCapacity = capacity - usedCapacity
            value = item.density * unusedCapacity
            usedCapacity += unusedCapacity
            total += value

        if usedCapacity == capacity:
            break
    print(total)

item1 = Item(20, 100)
item2 = Item(30, 120)
item3 = Item(10, 60)
items = [item1, item2, item3]

knapsack(items, 50)