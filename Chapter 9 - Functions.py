# Define a function my_function() with parameter x


def my_function(x):
    return x + 1


# Invoke the function

print(my_function(2))  # Output: 3
print(my_function(3 + 5))  # Output: 9

# Function Indentation
# Indentation is used to identify code blocks


def testfunction(number):
    # This code is part of testfunction
    print("Inside the testfunction")
    sum = 0
    for x in range(number):
        # More indentation because 'for' has a code block
        # but still part of he function
        sum += x
    return sum


# call the function

# what happen if i use this?
testfunction(10)

# and what happen if i use this?
print(testfunction(10))


# Function Parameters
def write_a_book(character, setting, special_skill):
    print(character + " is in " + setting + " practicing her " + special_skill)


# try to put some in it
# print(write_a_book())


# Multiple Parameters
def ready_for_school(backpack, pencil_case):
    if backpack == "full" and pencil_case == "full":
        print("I'm ready for school!")


# lets say the backpack is full but the pencil case is empty


# Function Arguments
def sales(grocery_store, item_on_sale, cost):
    print(grocery_store + " is selling " + item_on_sale + " for " + cost)


sales("The Farmer’s Market", "toothpaste", "$1")


# Function Keyword Arguments
def findvolume(length=1, width=1, depth=1):
    print("Length = " + str(length))
    print("Width = " + str(width))
    print("Depth = " + str(depth))
    return length * width * depth


# what happen if we didnt put any arguments?
print(findvolume())
# what happen if we put an arguments?
print(findvolume(1, 2, 3))
print(findvolume(length=5, depth=2, width=4))
print(findvolume(2, depth=3, width=4))


# Returning Multiple Values with variable
def square_point(x, y, z):
    x_squared = x * x
    y_squared = y * y
    z_squared = z * z
    # Return all three values:
    return x_squared, y_squared, z_squared


three_squared, four_squared, five_squared = square_point(3, 4, 5)
print(three_squared)
print(four_squared)
print(five_squared)

# scope variable
a = 5


def f1():
    a = 2
    print(a)


print(a)  # Will print 5
f1()  # Will print 2

# Global Variables
a = "Hello"


def prints_a():
    print(a)


# will print "Hello"
prints_a()


# returning value from function
def check_leap_year(year):
    if year % 4 == 0:
        return str(year) + " is a leap year."
    else:
        return str(year) + " is not a leap year."


year_to_check = 2018
returned_value = check_leap_year(year_to_check)
print(returned_value)  # 2018 is not a leap year.


# parameter as Local Variables
def fungsiku(value):
    print(value)


# Pass the value 7 into the function
fungsiku(7)

# Causes an error as `value` no longer exists
# print(value)
