#user defined exception

# class CustomError(Exception):
#     pass

# try:
#     ...
# except CustomError:
#     ...

class InvalidAgeException(Exception):
    def __init__(self,age,  message="You must be 18 years and above"):
        self.age = age
        self.message = message
        super().__init__(self.message)

# try:
#     user_age = int(input("How old are you?"))
#     if(user_age<18):  
#         raise InvalidAgeException
#     else:
#         print("You are eligible")
    
# except InvalidAgeException:
#     print("Exception Occured: Age not on the working age range")


user_age = int(input("How old are you?"))
if(user_age<18):
    raise InvalidAgeException(user_age)
else:
    print("Your age is permitted to work")