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
        return f"Brand : {self.brand}, Engine : {self.engine}"
    

engine1 = Engine(180)
engine2 = Engine(150)
engine3 = Engine(130)

car1 = Car('Toyota',engine1)
car2 = Car('Hundai',engine2)
car3 = Car('haval',engine3)

cars = [car1,car2,car3]

for i in cars:
    print(i)