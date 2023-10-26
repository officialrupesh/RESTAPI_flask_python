# print(dir(locals()["__builtins__"])) 

num1 = 0
num2 = 4

try:
    num = num2 / num1
    print(num)

except ZeroDivisionError as e:
    print("I cannot divide",e)

print("exception")