# Dictionaries
# Dictionaries is another kind of data type in Python in addition to integers, floats, strings, boolean etc.
# Dictionaries are enclosed in curly brackets
# Dictionaries data are stored as key:value pair.
# All keys inside the dictionary are supposed to be unique
# Values inside dictionary can be duplicate as well

x1 = {"name" : "Yom", "age" : 12, 364 : "test value", "test" : "test value"}
print(x1, "\n", type(x1), "\n")

x2 = {"name" : "Yom", "age" : 12, 364 : "test value", "test" : "test value", 364 : "another value"}
print(x2, "\n")

# check all keys in dictionary
print(x2.keys())

#check all values in dictionary
print(x2.values())

#check all items in a dictionary
print(x2.items())
print("\n")

# extract value from a dictionary
print(x2["name"])

# add new item to a dictionary
x2["profession"] = "Student"
print("\n")
print(x2)

#deleting items from a dictionary
print("\n")
del x2["age"]
print(x2)