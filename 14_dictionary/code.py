my_dictionary =  {"name": "value", "age" : 20, "address": "Nepal",(1,2): "This is tuple"}

# print(my_dictionary)


my_dictionary_2 = dict({"name":"Rupesh", "age": 25})

# print(my_dictionary_2)

# print(len(my_dictionary_2))

# print(my_dictionary_2["age"])

# Updating the dictionary

my_dictionary["addition"] = "variable"
my_dictionary.update({"rupesh":"name"})
my_dictionary.update({"name":"rupesh"})
# del my_dictionary["name"]
# my_dictionary.clear()
# print(my_dictionary)

# for item in my_dictionary:
#     print(my_dictionary[item])

for key,value in my_dictionary.items():
    print(key, value)