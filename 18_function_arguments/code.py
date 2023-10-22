# def variables(num1, num2):
#     print(f"num1 : {num1} num2: {num2} ")
#     sum = num1 + num2
#     print(f"Sum of {num1} and {num2} is {sum}")

# variables(2,10)


#parameters and arguement 
#parameter : when we pass anything to a function that is a parameter
#argument: whatever a function accepts is an argument ie num1,num2


#return type

# def ret(num1,num2) ->int:
#     sum  = num1 + num2
#     return sum

# total = ret(1,2)

# print(total)


def square_num(num):
    return num * num

my_numbers = [1,2,3,4]
square_of_numbers = [ square_num(num) for num in my_numbers]
print(square_of_numbers)