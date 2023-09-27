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
