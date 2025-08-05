'''8. ATM Machine Simulator:

Create a function that simulates an ATM machine.
Initialize an account with a starting balance.
Allow the user to perform transactions such as deposit, withdraw, and check balance.
Validate transactions against the account balance and available funds.
Provide appropriate feedback to the user for each transaction.
'''
from typing import Self
import re
from getpass import getpass

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Email(str): 

    def __new__(cls, email: str | Self) -> Self:

        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.fullmatch(pattern, email):
            raise ValueError(f"L'email: '{email}', non sembra risultare valida!")
        
        return str.__new__(cls, email)
    
class Account:

    _username:str
    _password:str
    _email:str

    def __init__(self, username:str, password:str, email:Email=None) -> None:

        self.setUsername(username)
        self.setEmail(email)
        self._password = password

    def setUsername(self, username:str) -> None:
        self._username = username

    def setEmail(self, email:Email | None) -> None:
        self._email = email 
    
    def getUsername(self) -> str:
        return self._username
    
    def getPassword(self) -> str:
        return self._password

    def getEmail(self) -> Email:
        return self._email 
    
    def changePasswordWithEmail(self, email:Email) -> str:
         
        if email == self._email:
            print(f"Email Validata ✅\nAdesso puoi cambiare password!")

            new_password = input("Inserisci la tua nuova password: ") # usare getpass per privacy
            self._password = new_password

    def changePassword(self, vecchia_password:str, nuova_password:str) -> str | None:
         
        if vecchia_password == self._password: 
            self._password = nuova_password
            print(f"Nuova password impostata!\nMi raccomando non dimenticarla!! 😉")

        elif vecchia_password != self._password and self._email != None:
            
            print(f"La password '{vecchia_password}' non corrisponde alla password attuale\nSe vuoi impostare una nuova password inserisci sotto la tua email")
            email = input("Inserisci la tua email: ")
            
            if email == self._email:
                self.changePasswordWithEmail(email)
            else:
                raise ValueError("Email inserita non valida")

        else:
            return f"❌ Impossibile cambiare la password, la vecchia password non corrisponde oppure email non impostata!"
             
    def __str__(self) -> str:
        return f"{color.BOLD + color.UNDERLINE} Informazioni Account {color.END}\n• Username: {self._username}\n• Password: *********\n• Email: ****************"


class ATM:

    _saldo:float = 0
    _validazione_account:bool = False

    def __init__(self, account: Account):
        self._account = account
        self._validazione_account = self.validateAccount()

    def validateAccount(self) -> bool:
        password_account = input("Inserisci la password per accedere all'ATM: ") # usare getpass per privacy

        if password_account == self._account.getPassword():

            print(f"{color.BOLD + color.GREEN} ✅ Accesso Eseguito! {color.END}\nBenvenuto {self._account.getUsername()}")
            return True

        else:
            print(f"{color.BOLD + color.RED} ❌ Accesso Negato! {color.END}\nPassword inserita errata")
            return False
        
    def depositMoney(self, money:float) -> str:

        if self._validazione_account == True:
            self._saldo += money
            return f"Soldi depositati con successo!"
        
        else:
            return f"Devi inserire la password per accedere a questa operazione!"
    
    def withdrawMoney(self, money:float) -> str:

        if self._validazione_account == True:

            if money > self._saldo:
                raise ValueError(f"Non possiedi questa somma di denaro!")
            
            else:
                self._saldo -= money 
                return f"Soldi prelevati con successo!"
            
        else:
            return f"Devi inserire la password per accedere a questa operazione!"

    def checkMoney(self) -> str:

        if self._validazione_account == True:
            return f"Questo è il tuo saldo: {self._saldo:.2f}"
        
        else:
            return f"Devi inserire la password per accedere a questa operazione!"
                