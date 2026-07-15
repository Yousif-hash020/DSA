class Student:
    def __init__(self, x, y):
        self.x = x
        self.y = y


student1 = Student('Yousaf', 158)

print(student1.x)
print(student1.y)


class Car:
    def __init__(self, brand, color = 'Black'):

        self.brand = brand
        self.color = color

        

new_Car = Car('toyita')

print(new_Car.color)
print(new_Car.brand)        