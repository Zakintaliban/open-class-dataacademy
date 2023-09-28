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
