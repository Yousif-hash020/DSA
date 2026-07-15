class Engine:
    def __init__(self, HP):
        self.HP = HP

    def __str__(self):
        return f"{self.HP} HP"
    
class Car:
    def __init__(self, brand , engine):
        self.brand = brand
        self.engine = engine
    

    def  __str__(self):
        return f"Brand : {self.brand} Engine : {self.engine}"
    

engine1 = Engine(180)

car1 = Car('Toyota',engine1)
print(car1)