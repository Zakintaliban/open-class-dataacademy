from functools import reduce

# Lambda functions
# Lambda functions are a powerful feature of Python that allow you to define anonymous functions.
# Anonymous functions are functions that do not have a name. They are often used as callback functions or as inline functions.

# Add two numbers
add = lambda x, y: x + y

# Print the sum of two numbers
print(add(1, 2))

# Filtering a list

# Lambda functions can be used to filter a list by removing certain elements.
# For example, the following code filters a list of numbers to only include even numbers:

# Filter a list of numbers to only include even numbers
numbers = [10, 5, 3, 2, 1]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Print the filtered list
print(list(even_numbers))

# Mapping a list

# Lambda functions can be used to map a list by applying a function to each element of the list.
# For example, the following code maps a list of numbers to their squares:

# Map a list of numbers to their squares
numbers = [1, 2, 3, 4, 5]

squared_numbers = map(lambda x: x * x, numbers)

# Print the mapped list
print(list(squared_numbers))

# Reducing a list

# Lambda functions can be used to reduce a list to a single value.
# For example, the following code reduces a list of numbers to their sum:

# Reduce a list of numbers to their sum
numbers = [1, 2, 3, 4, 5]

sum_of_numbers = reduce(lambda x, y: x + y, numbers)

# Print the reduced value
print(sum_of_numbers)


# higher order functions
# A function that takes a function as an argument and/or returns a function as a return value is called a higher-order function.
# or in short, a function using other functions as arguments.


# Recursive functions are functions that call themselves directly or indirectly.
# Higher-order functions are functions that can take other functions as arguments and/or return functions as a result.
def add_one(x):
    return x + 1


def apply_twice(func, x):
    return func(func(x))


angka = int(input("Masukkan angka: "))

# Apply the add_one() function twice to the number 5
result = apply_twice(add_one, angka)

print(result)


# map() function
# function takes a function and an iterable as arguments and returns a new iterable
# with the results of applying the function to each element of the iterable.
def square(x):
    return x * x


# Map the square function to the list [1, 2, 3, 4, 5]
squared_list = map(square, [1, 2, 3, 4, 5])

squared_list = list(squared_list)

print(squared_list)


# filter() function
# The filter() function takes a function and an iterable as arguments and returns a new iterable
# with the elements of the original iterable for which the function returns True.
def is_even(x):
    return x % 2 == 0


# Filter the list to only include even numbers
even_numbers = filter(
    is_even,
    [28, 93, 55, 72, 31, 18, 47],
)
even_numbers = list(even_numbers)

print(even_numbers)

# reduce()
# The reduce() function takes a function and an iterable as arguments and returns a single value
# by applying the function to each element of the iterable and returning the result.

sum_of_even_numbers = reduce(lambda x, y: x + y, [19, 20, 53, 46, 71, 62])

print(sum_of_even_numbers)

# The map() and filter() functions in Python return iterables. An iterable is an object that can be iterated over, such as a list, tuple, or string.
# If you want to get the actual values from the iterable, you need to convert it to a list using the list() function.
# This is because the map() and filter() functions are designed to be lazy,
# meaning that they don't actually evaluate the iterable until you need the values.
# If you don't convert the iterable to a list, you will get an object back. This object is a generator object,
# which is a type of iterable that can be used to generate values on the fly.
