



class ContactManager:

    def __init__(self, contacts:dict[str,list[str]]) -> None:

        self.contacts = contacts

    def create_contact(self, name:str, phone_numbers:list[str]) -> dict[str,list[str]] | str:

        if name in self.contacts:

            return f"Errore: il contatto {name} esiste già."
        
        else:

            self.contacts[name] = phone_numbers

            return {name : self.contacts[name]}
        
    def add_phone_number(self, contact_name:str, phone_number:str) -> dict[str,list[str]] | str:
        
        if contact_name not in self.contacts:

            return f"Errore: il contatto {contact_name} non esiste."
        
        elif phone_number in self.contacts[contact_name]:

            return f"Errore: il numero di telefono {phone_number} esiste già."
        
        else:

            self.contacts[contact_name].append(phone_number)

            return {contact_name : self.contacts[contact_name]}

    def remove_phone_number(self, contact_name:str, phone_number:str) -> dict[str,list[str]] | str:

        if contact_name not in self.contacts:

            return f"Errore: il contatto {contact_name} non esiste."
        
        elif phone_number not in self.contacts[contact_name]:

            return f"Errore: il numero di telefono {phone_number} non esiste."
        
        else:

            self.contacts[contact_name].remove(phone_number)

            return {contact_name : self.contacts[contact_name]}

    def update_phone_number(self, contact_name:str, old_phone_number:str, new_phone_number:str) -> dict[str,list[str]] | str:

        if contact_name not in self.contacts:

            return f"Errore: il contatto {contact_name} non esiste."
        
        elif old_phone_number not in self.contacts[contact_name]:

            return f"Errore: il numero di telefono {old_phone_number} non è presente."
        
        else:

            self.contacts[contact_name].remove(old_phone_number)
            self.contacts[contact_name].append(new_phone_number)

            return {contact_name : self.contacts[contact_name]}

    def list_contacts(self) -> list[str]:

        lista_di_contatti:list[str] = []

        for contatti in self.contacts.keys():

            lista_di_contatti.append(contatti)
        
        return lista_di_contatti

    def list_phone_numbers(self, contact_name:str) -> list[str] | str:

        lista_numeri_telefono:list[str] = []

        if contact_name not in self.contacts:

            return f"Errore: il contatto {contact_name} non esiste."
        
        else:

            for numeri in self.contacts[contact_name]:

                lista_numeri_telefono.append(numeri)

            return lista_numeri_telefono

    def search_contact_by_phone_number(self, phone_number:str) -> list[str] | str:

        lista_contatti_stesso_numero:list[str] = []

        for contatto, numero in self.contacts.items():

            if phone_number in numero:

                lista_contatti_stesso_numero.append(contatto)

                return lista_contatti_stesso_numero
            
            else:

                return "Nessun contatto trovato con questo numero di telefono!"
        
c:ContactManager = ContactManager({})

contatto1 = c.create_contact("Giuseppe", ["3349138566"])
print(contatto1)

contatto2 = c.create_contact("Giuseppe", ["3339128090"])
print(contatto2)

contatto3 = c.create_contact("Francesco", ["3475782375"])
print(contatto3)

print(c.contacts)
print(f"\n")

c.add_phone_number("Giuseppe", "3868754465")
print(contatto1)

print(c.add_phone_number("Mario", "3333337777"))
print(c.add_phone_number("Giuseppe", "3349138566"))
print(c.add_phone_number("Giuseppe", "3346758672"))

print(contatto1)
print("\n")

print(contatto1)
print(contatto3)

c.remove_phone_number("Giuseppe", "3349138566")
print(contatto1)

print(c.remove_phone_number("Francesco", "3333335555"))
print(c.remove_phone_number("Mario", "3333335555"))
print("\n")

print(c.update_phone_number("Giuseppe", "3349138566", "4444446666"))
print(c.update_phone_number("Mario", "3349138566", "4444446666"))
print("\n")

print(c.list_contacts())
print("\n")

c.add_phone_number("Giuseppe", "6666666666")
print(c.list_phone_numbers("Giuseppe"))

print(c.search_contact_by_phone_number("3349138566"))

print(c.search_contact_by_phone_number("3868754465"))