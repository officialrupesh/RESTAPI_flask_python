#List Comprehension

#List comprehension offers a shorter syntax

#when you want to create a new list based on the values of an existing list.

my_list = [1,2,3,4,5,6,7,8,9,10]

even = []

for number in my_list:
    if number % 2 == 0:
        even.append(number)

print(even)



# list_comprehension tech

odd = [number for number in my_list if number % 2 != 0]

print(odd)