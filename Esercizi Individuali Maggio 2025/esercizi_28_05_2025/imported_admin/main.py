'''
In a separate file main.py, import the classes, create a User and a Privileges instance, pass them to Admin, and call describe_user() and show_privileges() to verify everything works correctly.
'''

from users import Admin, User, Privileges

utente:User = User("Giovanni", "Mucciaccia", "Giovy29", "giovannimucciaccia29@gmail.com")
privilegi:Privileges = Privileges(False, False, True)

print(utente.describe_user())
print(privilegi.show_privileges())