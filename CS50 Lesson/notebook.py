print("Hello, world!")

name = input ("Name: ")
print("Hello, " + name)

=

name = input ("Name: ")
print(f"Hello, {name}")

n = float(input ("Number: "))

if n > 0:
    print("n is positive")
elif n < 0:
    print("n is not positive")  
else:
    print("n is zero")

Sequences

name = "Diogo"
print(name[3])

name = ["Diogo", "Antonio", "Sperandio", "Xavier"]
print(name[2])

name = ["Diogo", "Antonio", "Sperandio", "Xavier"]
print(name)

cordinateX = 10.0
cordinateY = 20.0

cordinate = (10.0, 20.0)

Lists

Define a list of names
names = ["Harry" , "Ron", "Hermione", "Ginny"]
print(names)
names.append("Draco")
print(names)
names.sort()
print(names)

sets

Create an empity set
s = set()
Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3) # just add once
print(s)
s.remove(2)
print(s)
print(f"The set has {len(s)} elements")

Loops

for i in [0, 1, 2, 3, 4, 5]:
    print(i)

for i in range(16):
    print(i)

names = ["Harry" , "Ron", "Hermione", "Ginny"]

for name in names:
    print(name)

name = "Harry"

for character in name:
    print(character)

dictionaries

houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
houses["Hermione"] = "Gryffindor"
print(houses)
print(houses["Draco"])

Functions

def square(x):
    return x * x

for i in range (10):
    print(f"The square of {i} is {square(i)}")

classes - template for a type of objective

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 8)

print(p.x)
print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
        
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry" , "Ron", "Hermione", "Ginny"]
for person in people:
    sucess = flight.add_passenger(person)
    if sucess:
        print(f"Added {person} to flight sucessfully.")
    else:
        print(f"No available seats fot {person}")

 decorators.py

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the functions.")
    return wrapper

@announce
def hello():
    print("hello, world!")

hello()

lambda

people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

def f(person):
    return person["name"]
people.sort(key=f)

people.sort(key=lambda person:["name"])

print(people)

exceptions

import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)

try:
    result = x / y 
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")