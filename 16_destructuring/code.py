#destructing : extracting some values from iterable to simple variable


# (a,b) =  (1,2)
# (c,d) = [3,4]
e,*f,g = [1,2,3,4,5,6]
# * : getting all the rest of element
# use of _: to ignore the value

i,*_ = [1,2,3,4,3,2]

#print(a)
# print(b)

# print(c)
# print(d)

print(f[2])
