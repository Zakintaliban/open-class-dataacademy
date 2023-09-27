# operasi aritmetika

result = 10 + 30
result = 40 - 10
result = 50 * 5
result = 16 / 4
result = 25 % 2
result = 5**3

# Plus-Equal Operator

counter = 0
counter += 10

# ini bentuk panjangnya

counter = 0
counter = counter + 10

# Modulo operations

# 8 bagi 4 hasilnya 2 sisa 0 jadi jawabannya 0
zero = 8 % 4

# 12 bagi 5 hasilnya 10 sisa 2 jadi jawabannya 2
nonzero = 12 % 5

# if Statement
test_value = 100

if test_value > 1:
    # Expression evaluates to True
    print("This code is executed!")

if test_value > 1000:
    # Expression evaluates to False
    print("This code is NOT executed!")

print("Program continues at this point.")

# elif Statement
pet_type = "fish"

if pet_type == "dog":
    print("You have a dog.")
elif pet_type == "cat":
    print("You have a cat.")
elif pet_type == "fish":
    # this is performed
    print("You have a fish")
else:
    print("Not sure!")

# else Statement
test_value = 50

if test_value < 1:
    print("Value is < 1")
else:
    print("Value is >= 1")

test_string = "VALID"

if test_string == "NOT_VALID":
    print("String equals NOT_VALID")
else:
    print("String equals something else!")

# boolean operator
is_true = True
is_false = False

print(type(is_true))
# will output: <class 'bool'>

# comparison operators
a = 2
b = 3
a < b  # evaluates to True
a > b  # evaluates to False
a >= b  # evaluates to False
a <= b  # evaluates to True
a <= a  # evaluates to True

# Equal operator

if "Yes" == "Yes":
    # evaluates to True
    print("They are equal")

if (2 > 1) == (5 < 10):
    # evaluates to True
    print("Both expressions give the same result")

c = "2"
d = 2

if c == d:
    print("They are equal")
else:
    print("They are not equal")

# Not Equals Operator

if "Yes" != "No":
    # evaluates to True
    print("They are NOT equal")

val1 = 10
val2 = 20

if val1 != val2:
    print("They are NOT equal")

if (10 > 1) != (10 > 1000):
    # True != False
    print("They are NOT equal")

# and Operator
True and True  # Evaluates to True
True and False  # Evaluates to False
False and False  # Evaluates to False
1 == 1 and 1 < 2  # Evaluates to True
1 < 2 and 3 < 1  # Evaluates to False
"Yes" and 100  # Evaluates to True

# or Operator
True or True  # Evaluates to True
True or False  # Evaluates to True
False or False  # Evaluates to False
1 < 2 or 3 < 1  # Evaluates to True
3 < 1 or 1 > 6  # Evaluates to False
1 == 1 or 1 < 2  # Evaluates to True

# not Operator
not True  # Evaluates to False
not False  # Evaluates to True
1 > 2  # Evaluates to False
not 1 > 2  # Evaluates to True
1 == 1  # Evaluates to True
not 1 == 1  # Evaluates to False
