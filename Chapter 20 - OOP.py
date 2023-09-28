# this lesson would be a little bit harder because to understand
# this lesson you need to know about class

# OOPs Concepts in Python
# Inheritance
# Polymorphism
# Encapsulation
# and many more


# inheritance
# Inheritance is the capability of one class to derive or inherit
# the properties from another class. The class that derives properties
# is called the derived class or child class and the class from which
# the properties are being derived is called the base class or parent class.
class Cat:
    # def init is a constructor method
    # and self is a reference to the current instance of the class
    # so i.e. self.name is the name of the current instance of the class
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        return f"My name is {self.name} and I am a {self.color} cat."

    def meow(self):
        print("Meow!")

    def eat(self, food):
        print(f"{self.name} is Eating {food}")

    def sleep(self):
        print("Sleeping...")


class Irl_Cat(Cat):
    def __init__(self, name, age, color, race, weight):
        super().__init__(name, age, color)
        self.race = race
        self.weight = weight

    def __str__(self):
        return f"My name is {self.name} and I am a {self.color} {self.race} cat."

    def weight(self):
        print(f"{self.name} is {self.weight} kg")


# Create a new cat object
garfield = Cat("Garfield", 5, "orange")
gumball = Cat("Gumball", 3, "blue")

# Create a new Persian cat object
persian_cat = Irl_Cat("Snowball", 2, "white", "persian", 4.5)

print(garfield)
print(gumball)
print(persian_cat)

# Call the meow() method on the cat object
garfield.meow()
gumball.meow()
persian_cat.meow()

# Call the eat() method on the cat object
garfield.eat("lasagna")
gumball.eat("cheese")
persian_cat.eat("tuna")

# Call the sleep() method on the cat object
garfield.sleep()
gumball.sleep()
persian_cat.sleep()

# call the weight attribute on the persian_cat object
persian_cat.weight()

# call the race attribute on the persian_cat object
print(persian_cat.race)


# polymorphism
# Polymorphism simply means having many forms.
# For example, we need to determine if the given species of birds fly or not,
# using polymorphism we can do this using a single function.


class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")


class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

# encapsulation
# Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
# It describes the idea of wrapping data and the methods that work on data within one unit.
# This puts restrictions on accessing variables and methods directly
# and can prevent the accidental modification of data.
# To prevent accidental change, an object’s variable can only be changed by an object’s method.
# Those types of variables are known as private variables.


class Lizard:
    def __init__(self, name, color, size):
        self.__name = name
        self.__color = color
        self.__size = size

    def __str__(self):
        return f"My name is {self.__name} and I am a {self.__color} lizard. and I am {self.__size}"

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_color(self):
        return self.__color

    def set_color(self, new_color):
        self.__color = new_color

    def get_size(self):
        return self.__size

    def set_size(self, new_size):
        self.__size = new_size

    def __eat(self, food):
        print(f"{self.__name} is eating {food}.")

    def eat(self, food):
        self.__eat(food)

    def __sleep(self):
        print(f"{self.__name} is sleeping.")

    def sleep(self):
        self.__sleep()


# Create a new lizard object
lizard = Lizard("Lizzy", "green", "small")

print(lizard)

# Get the lizard's name
lizard.get_name()

# Set the lizard's color
lizard.set_color("blue")

# Get the lizard's color
color = lizard.get_color()

# Print the lizard's color
print(color)

# Call the lizard's eat() method
lizard.eat("flies")

# Call the lizard's sleep() method
lizard.sleep()
