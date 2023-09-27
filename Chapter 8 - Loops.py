"""
for <temporary variable> in <list variable>:
  <action statement>
  <action statement>
"""
# each num in nums will be printed below
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

# Python Loops with range().
# Print the numbers 0, 1, 2:
for i in range(3):
    print(i)

# Print "WARNING" 3 times:
for i in range(3):
    print("WARNING")

# break statement
numbers = [0, 254, 2, -1, 3]

for num in numbers:
    if num < 0:
        print("Negative number detected!")
        break
    print(num)

# 0
# 254
# 2
# Negative number detected!

# continue statement
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

# Print only positive numbers:
for i in big_number_list:
    if i < 0:
        continue
    print(i)

# nested loops

groups = [["Jobs", "Gates"], ["Newton", "Euclid"], ["Einstein", "Feynman"]]

# This outer loop will iterate over each list in the groups list
for group in groups:
    # This inner loop will go through each name in each list
    for name in group:
        print(name)

"""
danger zone: Infinite Loop
"""

# i = 0
# while True:
#     print(i)
#     i += 1

# This loop will print the numbers from 0 to 9 to the console.
# However, the condition `i < 10` will never be false,
# so the loop will continue to execute forever.

"""
end of danger zone
"""

# Python while Loops
# This loop will only run 1 time
hungry = True
while hungry:
    print("Time to eat!")
    hungry = False

# This loop will run 5 times
i = 1
while i < 6:
    print(i)
    i = i + 1
