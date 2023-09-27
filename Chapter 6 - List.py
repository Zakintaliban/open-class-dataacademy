# contoh list
primes = [2, 3, 5, 7, 11]
print(primes)

empty_list = []

# menggabungkan 2 list
items = ["cake", "cookie", "bread"]
total_items = items + ["biscuit", "tart"]
print(total_items)
# Result: ['cake', 'cookie', 'bread', 'biscuit', 'tart']

# method append atau nambah
orders = ["daisies", "periwinkle"]
orders.append("tulips")
print(orders)
# Result: ['daisies', 'periwinkle', 'tulips']

# indexing(?)

names = ["Roger", "Rafael", "Andy", "Novak"]
print(names[2])  # siapa?

# negative list

soups = ["minestrone", "lentil", "pho", "laksa"]
# To select the last element, my_list[-1]:
# Untuk memilih elemen terakhir dalam daftar my_list, gunakan indeks -1.
# Ini akan mengembalikan elemen terakhir dari daftar.

# To select the last three elements, my_list[-3:].
# Untuk memilih tiga elemen terakhir dalam daftar my_list, gunakan slicing dengan indeks -3:.
# Ini akan mengembalikan tiga elemen terakhir dari daftar.

# To select everything except the last two elements, my_list[:-2].
# Untuk memilih semua elemen kecuali dua elemen terakhir dalam daftar my_list, gunakan slicing dengan :-2.
# Ini akan mengembalikan semua elemen dalam daftar kecuali dua elemen terakhirnya.

soups[-1]  # 'laksa'
soups[-3:]  # 'lentil', 'pho', 'laksa'
soups[:-2]  # 'minestrone', 'lentil'

# List Method .remove()
shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]

# Removes the first occurance of "Chris"
shopping_line.remove("Chris")
print(shopping_line)

# Output
# ["Cole", "Kip", "Sylvana", "Chris"]

# List Method .count()
backpack = ["pencil", "pen", "notebook", "textbook", "pen", "highlighter", "pen"]
numPen = backpack.count("pen")

print(numPen)
# Output: 3

# Determining List Length with len()
knapsack = [2, 4, 3, 7, 10]
size = len(knapsack)
print(size)
# Output: 5

# List Method .sort()
exampleList = [4, 2, 1, 3]
exampleList.sort()
print(exampleList)
# Output: [1, 2, 3, 4]

# list method sorted()
unsortedList = [4, 2, 1, 3]
sortedList = sorted(unsortedList)
print(sortedList)
# Output: [1, 2, 3, 4]

# whats the difference between sort and sorted?
# sorted() returns a new sorted list, leaving the original list unaffected.

# list slicing
tools = ["pen", "hammer", "lever", "saw"]
tools_slice = tools[1:3]  # ['hammer', 'lever']
tools_slice[0] = "nail"

# Original list is unaltered:
print(tools)  # ['pen', 'hammer', 'lever', 'saw']

# List Method .insert()
# Here is a list representing a line of people at a store
store_line = ["Karla", "Maxium", "Martim", "Isabella"]

# Here is how to insert "Vikor" after "Maxium" and before "Martim"
store_line.insert(2, "Vikor")

print(store_line)
# Output: ['Karla', 'Maxium', 'Vikor', 'Martim', 'Isabella']

# List Method .pop()
cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]

# Pop the last element
removed_element = cs_topics.pop()

print(cs_topics)
print(removed_element)

# Output:
# ['Python', 'Data Structures', 'Balloon Making', 'Algorithms']
# 'Clowns 101'

# Pop the element "Baloon Making"
cs_topics.pop(2)
print(cs_topics)

# Output:
# ['Python', 'Data Structures', 'Algorithms']

# 2D list

# A 2D list of names and hobbies
class_name_hobbies = [
    ["Jenny", "Breakdancing"],
    ["Marcus", "Photography"],
    ["Grace", "Soccer"],
]

# The sublist of Jenny is at index 0. The hobby is at index 1 of the sublist.
class_name_hobbies[0][1] = "Meditation"
print(class_name_hobbies)

# Output
# [["Jenny", "Meditation"], ["Alexus", "Photography"], ["Grace", "Soccer"]]
# now what if u want to change grace to something else?
class_name_hobbies[-1][0] = "Kim"
print(class_name_hobbies)

# 2D list of people's heights
# Access the sublist at index 0, and then access the 1st index of that sublist.
Aurelius = class_name_hobbies[1][0]
print(Aurelius)

# Output
# Marcus
