# Accessing and writing data in a Python dictionary
my_dictionary = {
    "song": "Estranged",
    "artist": "Guns N' Roses",
    "genre": "Rock",
    "year": 1991,
}
print(my_dictionary["song"])
my_dictionary["song"] = "Paradise City"
print(my_dictionary["song"])

# Merging dictionaries with the .update() method in Python
dict1 = {"color": "blue", "shape": "circle"}
dict2 = {"color": "red", "number": 42}

dict1.update(dict2)
print(dict1)
# dict1 is now {'color': 'red', 'shape': 'circle', 'number': 42}

# Dictionary value types
dictionary = {
    1: "hello",
    "two": True,
    "3": [1, 2, 3],
    "Four": {"fun": "addition"},
    5.0: 5.5,
}
print(dictionary)

# Dictionary Key-Value Methods
ex_dict = {
    "a": "anteater",
    "b": "bumblebee",
    "c": "cheetah",
    "d": "dolphin",
    "e": "elephant",
}

ex_dict.keys()
# dict_keys(["a","b","c","d","e"])

ex_dict.values()
# dict_values(["anteater", "bumblebee", "cheetah", "dolphin", "elephant"])

ex_dict.items()
# dict_items([("a","anteater"),("b","bumblebee"),("c","cheetah"),("d","dolphin"),("e","elephant")])

# get() Method for Dictionary
# without default
my_dict = {"name": "Victor"}
print(my_dict.get("name"))
# returns "Victor"

print(my_dict.get("nickname"))
# returns None

# with default
my_dict.get("nickname", "nickname is not a key")
# returns "nickname is not a key"

# The .pop() Method for Dictionaries in Python
famous_museums = {
    "Washington": "Smithsonian Institution",
    "Paris": "Le Louvre",
    "Athens": "The Acropolis Museum",
}
famous_museums.pop("Athens")
print(famous_museums)  # {'Washington': 'Smithsonian Institution', 'Paris': 'Le Louvre'}

# sets
# Sets are unordered collections of unique values. Sets are created using curly braces {}

my_set = {1, 2, 3, 4, 5}

# Adding and removing elements from a set

my_set.add(6)
my_set.remove(1)

print(my_set)  # Prints {2, 3, 4, 5, 6}

# Checking if an element is in a set

print(2 in my_set)  # Prints True

# Set operations

my_set1 = {1, 2, 3, 4, 5}
my_set2 = {3, 4, 6, 8}

# Union of two sets
my_union = my_set1.union(my_set2)
print(my_union)  # Prints {1, 2, 3, 4, 5, 6, 8}

# Intersection of two sets
my_intersection = my_set1.intersection(my_set2)
print(my_intersection)  # Prints {3, 4}

# Difference of two sets
my_difference = my_set1.difference(my_set2)
print(my_difference)  # Prints {1, 2, 5}
