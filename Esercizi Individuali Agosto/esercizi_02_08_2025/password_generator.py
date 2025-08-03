'''
6. Password Generator:

Create a function that generates a random password with a specified length and desired character types (lowercase letters, uppercase letters, numbers, symbols).
Allow the user to specify the password length and desired character types.
Generate and return a random password that meets the user's criteria.
'''

from random import *
import random

def RandomPasswordGenerator(lenght:int, character_types:str | int) -> str:

    if lenght <= 0 or isinstance(lenght, float):
        raise ValueError("La password non può avere lunghezza 0, minore di 0 e non può essere un numero decimale")
    
    characters:list[str] = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    special_characters:list[int | str | int, str] = []
    random_password:list[int | str | int, str] = []

    for letters in character_types:
        special_characters.append(letters)

    for char in special_characters:
        random_password.append(char)

    for i in range(lenght - len(special_characters)):

        i = random.sample(characters,1)[0]
        random_password.append(i)
    
    shuffle(random_password)
        
    return ''.join(random_password)

print(RandomPasswordGenerator(12, "@!?=12__"))
    

    

