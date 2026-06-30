#====================task======================

class Car:
    def __init__(self, name, model, color, price, quantity):
        self.name = name
        self.model = model
        self.color = color
        self.price = price
        self.quantity = quantity

# Objects
obj = Car("Tata", "Punch", "Black", 1000, 10)
obj1 = Car("Tata", "Punch", "White", 100, 4)

# List of objects
x = [obj, obj1]

grand_total = 0

for i in x:
    print("Name      :", i.name)
    print("Model     :", i.model)
    print("Color     :", i.color)
    print("Price     :", i.price)
    print("Quantity  :", i.quantity)

    total = i.quantity * i.price
    print("Total     :", total)

    grand_total += total
    print("=========================")

print("Grand Total :", grand_total)