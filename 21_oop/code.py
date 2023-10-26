#python oop
#class and object

# class className:
#     class defination


#attribute,object,class
# class Bike:
#     name=""
#     gear=0

# pulsar = Bike()

# yamaha = Bike()

# pulsar.name = "Pulsar 1890"

# print(pulsar.name)

# class Room:
#     length: 0
#     breadth: 0
    
#     def calculate_area(self):
#         print(f"Area of Room:= {self.length * self.breadth} ")

# dining_room = Room()
# dining_room.length = 20
# dining_room.breadth = 100

# dining_room.calculate_area()

#ASSIGN VARIABLE USING CONSTRUCTOR

class Human:
    name:""
    age:0
    #dunder method
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"Name is {name} and age is {age}")
rupesh = Human("Rupesh",24)

