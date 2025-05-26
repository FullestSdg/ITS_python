# Write a function validate_password(password) that checks if a password meets certain criteria
# (i.e., minimum length of 20 characters, at least three uppercase characters, and at least four special characters). 
# Raise a custom exception (e.g., InvalidPasswordError) for invalid passwords.

class InvalidPasswordError(Exception):
    """Password non valida!"""

def validate_password(password:str):

    caratteri_speciali:list[str] = ["~","!","@","#","$","%","","^","&","*","_","-","+","=","`","|",":",";","'","''","<",">",",",".","?","/"]
    numero_caratteri_maiuscoli = 0

    for letters in password:

        if letters == letters.upper():
            numero_caratteri_maiuscoli += 1
        
        else:
            continue
    
    if len(password) >= 20 and numero_caratteri_maiuscoli >= 3:

        contatore_caratteri_speciali = 0

        while contatore_caratteri_speciali >= 4:

            for letters in password:

                if letters in caratteri_speciali:

                    contatore_caratteri_speciali += 1   
                    return "Password valida" 

                else:
                    raise InvalidPasswordError
    
    else:
        raise InvalidPasswordError
    
    


password_prova = validate_password("CiCiaoCIAOciaociaociao1234!!!!")
print(password_prova)




