from ATM_machine import *
from getpass import getpass

email = Email("sdgsergiodg20@gmail.com")
account = Account("FullestSdg", "FrancescoTotti92_")
print(account.getUsername(), account.getPassword(), account.getEmail())

account.setUsername("Sergio92_")
account.setEmail("FrancescoTotti_12@libero.it")

print(account.getUsername(), account.getPassword(), account.getEmail())

print("\n")

# FUNZIONA!

# account.changePassword("almergo", "VamosRagaForzaGiuve92") 
# print(account.getPassword()) 

# dovrebbe funziona ma c'è un "None" sospetto
# Aggiornato [05/08/2025] "Ho capito il perchè del None sospetto (quando chiamo il metodo e va a buon fine giustamente ritorna none)"

# print(account.changePasswordWithEmail("FrancescoTotti_12@libero.it")) 
# print(account.getPassword()) 

account2 = Account("Verstappen69", "TUDUDUDU_")

print(account2.changePassword("TUDU", "LECLERC_E_MEGLIO!"))
print("")
print(account)
print("")
print(account.getPassword())

# Grazie a chatgpt ho usato getpass di getpass per mettere in input la password in modo che non si veda 
# però farò in modo che si veda per comodità

machine = ATM(account)

print(machine.checkMoney())
try:
    print(machine.withdrawMoney(10))
except ValueError as e:
    print(f"⚠️ Errore: {e}")

print(machine.depositMoney(568))
print(machine.withdrawMoney(68))
print(machine.checkMoney())

