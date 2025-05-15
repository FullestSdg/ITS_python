'''
PARTE 1
Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo). 
La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
 
PARTE 2
Scrivi una funzione chiamata update_contact() che accetta il dizionario creato,
il nome e cognome del contatto da aggiornare, e il dettaglio facoltativo da aggiornare.
Questa funzione dovrebbe aggiornare il dizionario del contatto.
'''

def create_contact(name: str, email: str=None, telefono: int=None) -> dict:

    return {"profile" : name, "email" : email, "telefono": telefono}
    

def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    pass

profilo = create_contact("Sergio De Guidi", "sdgsergiodg20@gmail.com", 3349138566)
print(profilo)