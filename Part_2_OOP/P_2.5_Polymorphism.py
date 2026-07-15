class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def __str__(self):
        return f"Brand : {self.brand}, Color: {self.color}"
    def start(self):
        print("This car strat with key")

class Electric:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def __str__(self):
        return f"Brand; {self.brand}, Color:{self.color} "
    def start(self):
        print("this car strats by pushing button")    

car1 = Car('Toyota', 'red')
print(car1)
car1.start()
e1 = Electric('tesla', 'white')
print(e1)
e1.Start()