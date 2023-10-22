#while loop

#runs a block of code until a certain condition is met

# print("My name is Rupesh")


value = 0

# while value < 5:
#     print(f"{value} is the current value")
#     value = value + 1


#break 

#breaks the operation once the requirement is met for example in the below example: after counter is equals to 3
# the printer stops printnig the counter as the requirement is met

# counter = 0 
# while ( counter < 5):
#     if(counter > 3):
#         break
#     print(counter)
#     counter = counter + 1


#continue statement

# counter = 0 
# while ( counter < 5):
#     counter = counter + 1
#     if(counter == 3):
#         continue
#     print(counter-1)

#else
counter = 0
while counter <= 5:
    print("My name is Rupesh",counter)
    break
    counter = counter + 1

else:
    print("Else")