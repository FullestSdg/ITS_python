'''
Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, and call both methods for each user.
'''

class User:

    def __init__(self, first_name:str, last_name:str, password:str, years_old:int) -> None:

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.years_old = years_old
    
    def describe_user(self) -> str:

        return f"Hey {self.first_name} {self.last_name}, you are {self.years_old} and your password is {self.password}"
    
    def greet_user(self) -> str:

        return f"Today is your birthday {self.first_name,self.last_name}"
    
u1:User = User("Sergio", "De Guidi", "Esdrongo", 21)
u2:User = User("Giovanni", "De Guidi", "Ciao1234", 17)

print(u1.describe_user())

