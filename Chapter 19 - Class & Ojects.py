# create a class
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


# Create a new cat object
garfield = Cat("Garfield", 5, "orange")
gumball = Cat("Gumball", 3, "blue")

print(garfield)
print(gumball)

# Call the meow() method on the cat object
garfield.meow()
gumball.meow()

# Call the eat() method on the cat object
garfield.eat("lasagna")
gumball.eat("cheese")

# Call the sleep() method on the cat object
garfield.sleep()
gumball.sleep()
