name_list = ["Apple","Mango","Banana"]
# name_set = {"Apple","Mango","Banana"}
# name_tuple = ("Apple","Mango","Banana") 

# caseSensitive
ask_question = input("What is your favourite Fruit?")

if ask_question in name_list:
    print("Your favourite Fruit is available")
else:
    print("Sorry, Currently your favourite fruit is out of stock")