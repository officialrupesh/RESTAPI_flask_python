#functions : reusable block of code that executes a certain functionality when it is called
# real life example: After certain minutes a class session ends after bell rings and new class starts. it occurs at exact time
# so yo ta euta function set gare jasto vo ni ta 45 minutes paxi bell bajaunu parne reusable 


#Types of function
#1. Standard Library Function
#2. User Defined function

# In python, function is defined using "def"
# For example

# def my_function():
#     print("true")

# my_function()

# def multiply():
#     a=input("Provide first number")
#     b = input("Provide second number")
#     print(f"Sum of two number is {int(a)*int(b)} ")
# multiply()


def sum():
    a=int(input("Provide first number"))
    b = int(input("Provide second number"))
    print(f"Sum of two number is {a * b} ")
sum()