class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __str__(self):
        return self.brand + " " + self.color
    
car1 = Car('Toyota_Grandi', 'Supervite')
        
print(car1)