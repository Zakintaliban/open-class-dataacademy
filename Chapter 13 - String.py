# fstring

name = "Jayceon"
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")

# escaping characters
txt = 'She said "Never let go".'
print(txt)  # She said "Never let go".

# or like this:
# txt = "She said \"Never let go\"."
# print(txt) # She said "Never let go".

# The in Syntax
game = "Popular Nintendo Game: Mario Kart"

print("l" in game)  # Prints: True
print("x" in game)  # Prints: False

# Indexing and Slicing Strings
str = "yellow"
str[1]  # => 'e'
str[-1]  # => 'w'
str[4:6]  # => 'ow'
str[:4]  # => 'yell'
str[-3:]  # => 'low'

# Iterate String

str = "hello"
for c in str:
    print(c)

# h
# e
# l
# l
# o

# Built-in Function len()
length = len("Hello")
print(length)
# Output: 5

colors = ["red", "yellow", "green"]
print(len(colors))
# Output: 3

# String Concatenation
x = "One fish, "
y = "two fish."

z = x + y

print(z)
# Output: One fish, two fish.

# IndexError
fruit = "Berry"
indx = fruit[6]
print(indx)
# Output: IndexError: string index out of range

# Python String .format()
msg1 = "Fred scored {} out of {} points."
msg1.format(3, 10)
# => 'Fred scored 3 out of 10 points.'

msg2 = "Fred {verb} a {adjective} {noun}."
msg2.format(adjective="fluffy", verb="tickled", noun="hamster")
# => 'Fred tickled a fluffy hamster.'

# String Method .lower()
greeting = "Welcome To Chili's"

print(greeting.lower())
# Prints: welcome to chili's

# String Method .strip()
text1 = "   apples and oranges   "
text1.strip()  # => 'apples and oranges'

text2 = "...+...lemons and limes...-..."

# Here we strip just the "." characters
text2.strip(".")  # => '+...lemons and limes...-'

# Here we strip both "." and "+" characters
text2.strip(".+")  # => 'lemons and limes...-'

# Here we strip ".", "+", and "-" characters
text2.strip(".+-")  # => 'lemons and limes'

# String Method .title()
my_var = "dark knight"
print(my_var.title())

# Prints: Dark Knight

# String Method .split()
text = "Silicon Valley"

print(text.split())
# Prints: ['Silicon', 'Valley']

print(text.split("i"))
# Prints: ['S', 'l', 'con Valley']

# Python string method .find()
mountain_name = "Mount Kilimanjaro"
print(mountain_name.find("o"))  # Prints 1 in the console.

# String replace
fruit = "Strawberry"
print(fruit.replace("r", "R"))

# StRawbeRRy

# String Method .upper()
dinosaur = "T-Rex"

print(dinosaur.upper())
# Prints: T-REX

# String Method .join()
x = "-".join(["Codecademy", "is", "awesome"])

print(x)
# Prints: Codecademy-is-awesome
