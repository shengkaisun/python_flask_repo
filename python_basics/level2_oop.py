import math

x = 'outside'
def report():
    # Grab the global levl x variable
    #global x
    x = 'inside'
    return x


print(report())
print(x)

# LEGB RULE
# Local -> Enclosing -> Global -> Built in
# Local
def report():
    x = 'local'
    print(x)

# Enclosing
x = 'This is global level'
def enclosing():
    # x = 'Enclosing level'
    def inside():
        x = 'local'
        print(x) 
    inside()

enclosing()

# Object oriented programming
mylist = [1,2,3]
mylist.append(4)
print(type(mylist))

class Sample():
    pass

x = Sample()
print(type(x))

class Dog():
    # Class object attributes
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

x = Dog('Huskie', 'Sam')
new_dog = Dog('Golden', 'Cindy')
print(type(x.breed))
print(x.breed) # string
print(x.name)
print(x.species)

# Methods & inheritents
class Circle():
    pi = math.pi
    def __init__(self, radius=1):
        self.radius = radius
    
    def area(self):
        return self.radius**2 * self.pi

    def circumference(self):
        return 2 * self.pi * self.radius

mycircle = Circle(10)
print(mycircle.radius)
print(mycircle.area())
print(mycircle.circumference())

# Inheritence 
class Animal():
    def __init__(self, fur):
        self.fur = fur
        print('Animal created!')
    
    def report(self):
        print('Animal')
    
    def eat(self):
        print('Eating!')

class Dog(Animal):
    def __init__(self, fur):
        Animal.__init__(self, fur)
        print('Dog created!')
    
    def report(self):
        print('I am a dog!')

a = Animal('fuzzy')
a.eat()
a.report()

d = Dog('fuzzy')
d.eat()
d.report()

# Built in functions
len([1,2,3])
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __repr__(self):
        # used for print() -- string representation of the object
        return f"Title: {self.title}, Author: {self.author}"
    
    def __len__(self):
        return self.pages


mybook = Book("Python rocks!", 'Eric', 241)
print(mybook)

length_book = len(mybook)
print(length_book)