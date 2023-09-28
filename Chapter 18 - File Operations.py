# there are many way to read:
# a file named "zakin", will be opened with the reading mode.
file = open("zakin.txt", "r")

# This will print every line one by one in the file
for each in file:
    print(each)

# there are many ways to write, but lets move on

# this will write a file named "hadi" with the writing mode.

file = open("hadi.txt", "w")
file.write("Afah iyah?")
file.close()
