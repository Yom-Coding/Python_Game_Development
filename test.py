x2 = {"name" : "Yom", "age" : 12, 364 : "test value", "test" : "test value", 364 : "another value"}
print(x2, "\n")

# check all keys in dictionary
print(x2.keys())

list_data = list(x2.keys())
print (list_data, type(list_data))

list_data1 = list(x2.values())
print (list_data1, type(list_data1))

list_dictionary = list(x2)
print (list_dictionary, type(list_dictionary))

test = {}

test["name"] = "Yom"
test["Age"] = 12

print(test)