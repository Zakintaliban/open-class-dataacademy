# Handling Exceptions with Try/Except/Finally
# put unsafe operation in try block
try:
    print("code start")

    # unsafe operation perform
    print(1 / 0)

# if error occur the it goes in except block
except:
    print("an error occurs")

# final code in finally block
finally:
    print("end")

# Output:
# code start
# an error occurs
# end

# Raising exceptions for a predefined condition
# try for unsafe code
try:
    amount = 1999
    if amount < 2999:
        # raise the ValueError
        raise ValueError("please add money in your account")
    else:
        print("You are eligible to purchase DSA Self Paced course")

# if false then raise the value error
except ValueError as e:
    print(e)

# Output:
# please add money in your account
