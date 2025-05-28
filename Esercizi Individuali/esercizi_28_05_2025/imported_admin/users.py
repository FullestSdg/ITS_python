'''
9-11. Imported Admin: Create a module users.py containing three classes:

User: stores first_name, last_name, username, and email; includes describe_user() and greet_user() methods.
Privileges: holds a list of privileges and a method show_privileges() to display them.
Admin: stores a User instance and a Privileges instance as attributes.
In a separate file main.py, import the classes, create a User and a Privileges instance, pass them to Admin, and call describe_user() and show_privileges() to verify everything works correctly.

'''

class User:

    def __init__(self, first_name:str, last_name:str, username:str, email:str) -> None:

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self) -> str:

        return f"Hello {self.first_name} {self.last_name}!\nYour current username is: {self.username}\nYour current email is: {self.email}"
    
    def greet_user(self) -> str:

        return f"Welcome back {self.username}!"
    
class Privileges:

    def __init__(self, banning_users:bool, muting_users:bool, warning_users:bool) -> None:

        self.banning_users = banning_users
        self.muting_users = muting_users
        self.warning_users = warning_users
    
    def show_privileges(self):

        return {"banning_users" : self.banning_users, "muting_users": self.muting_users, "warning_users": self.warning_users}
    
class Admin:

    def __init__(self, utente1:User = User("Giovanni", "Mucciaccia", "Giovy29", "giovannimucciaccia29@gmail.com"), privilegi1:Privileges = Privileges(False, False, True)) -> None:

        self.utente1 = utente1
        self.privilegi1 = privilegi1

