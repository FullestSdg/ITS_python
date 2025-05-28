'''
9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
'''

class User:

    def __init__(self, first_name:str, last_name:str, password:str, years_old:int, login_attempts:int) -> None:

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.years_old = years_old
        self.login_attempts = login_attempts
    
    def describe_user(self) -> str:

        return f"Hey {self.first_name} {self.last_name}, you are {self.years_old} and your password is {self.password}"
    
    def greet_user(self) -> str:

        return f"Welcome back {self.first_name} {self.last_name}!"
    
    def increment_login_attempts(self) -> None:

        self.login_attempts += 1
    
    def reset_login_attempts(self) -> None:

        self.login_attempts -= self.login_attempts
    
   
u1:User = User("Sergio", "De Guidi", "Esdrongo", 21, 10)
u2:User = User("Giovanni", "De Guidi", "Ciao1234", 17, 10)

print(u1.login_attempts)

u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
print(u1.login_attempts)

u1.reset_login_attempts()
print(u1.login_attempts)