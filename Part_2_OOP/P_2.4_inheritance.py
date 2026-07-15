class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __str__(self):
        return f"Brand:{self.brand}, Color:{self.color}"

class Electric(Car):
    def __init__(self, brand, color, baterry_size):
        super().__init__(brand, color)
        self.baterry_size = baterry_size
    def __str__(self):
         return f"Bradn:{self.brand}, color:{self.color}, baterry_size:{self.baterry_size}"

car1 = Car('Toyota', 'red')

e1 = Electric('Toyota', 'red', '20v')

print(e1)
print(car1)

