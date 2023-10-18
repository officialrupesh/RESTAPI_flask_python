#list

l= ["Learn", "Python", "Rupesh"] 
# List with items
#In list we maintain an order

# accessing first item
# print(l[0])
# trying to get element at index 0

# append
l.append("Raut")
print(l)
l.append("extra")
# remove
# l.remove("Raut")
l.remove("extra")
print(l)

#tuples

t = ("Learn", "Python", "Rupesh")
# t.append("Raut")
print(t)

# diff between tuples and list is in list we can change elemennt, update t hem, but in tuple cannot update, immutable

print(t[0])

# set

s = {"Learn", "Python", "Rupesh"}   
# we cannot have dublicate elment in set
#we dont mainain any order

# print(s[0])


# we dont have append but we have add
# s.add("Raut")
# print(s)

# s.remove("Raut")
# print(s)
# s.add("Rupesh")
# print(s)

s.add("Python")
print(s)