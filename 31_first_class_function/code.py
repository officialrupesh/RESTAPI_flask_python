#Python first class function

# def func(num):
#     return num * 2

# my_func = func

# print(my_func(5))
# print(func)

# def shout(text):
#     return text.upper()

# def whisper(text):
#     return text.lower()

# #HOF higher order function

# def greet(func):
#     greeting = func("Hi There") 
#     print(greeting)

# greet(whisper)

def first_child():
    return "Hey First Child"

def second_child():
    return "Hey Second child"


def parent(num):
    if(num == 1):
        return first_child()    
    else:
        return second_child

my_parent = parent(2)

print(my_parent)
# print(my_parent())