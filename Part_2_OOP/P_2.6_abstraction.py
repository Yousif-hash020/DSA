from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def Start(self):
        print("this function help to srat the vehcle")

class Car(Vehicle):
    def Start(self):
        print("car starts with key")

class Electric(Vehicle):
    def Start(self):
        print("car starts with pushing button")

car1 = Car()
car2 = Electric()

car1.Start()
car2.Start()
