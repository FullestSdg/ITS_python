from ATM_machine import *

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
# Aggiornato "Ho capito il perchè del None sospetto (quando chiamo il metodo e va a buon fine giustamente ritorna none)"

# print(account.changePasswordWithEmail("FrancescoTotti_12@libero.it")) 
# print(account.getPassword()) 

account2 = Account("Verstappen69", "TUDUDUDU_")

print(account2.changePassword("TUDU", "LECLERC_E_MEGLIO!"))