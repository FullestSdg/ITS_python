# dal file persona.py importa la classe Persona
'''from persona import Persona

sdg:Persona = Persona("Sergio", "De Guidi", 21)

print(sdg)
print(f"{sdg.name}\n{sdg.last_name}\n{sdg.age}")

# sfrutto la funzione displayData della classe Persona per visualizzare i dati relativi alla funzione

sdg.displayData()
'''

from persona2 import Persona

sdg:Persona = Persona()

sdg.displayData()

# imposto il nome della persona sdg

sdg.setName("Sergio")
sdg.displayData()

# imposto il cognome della persona sdg

sdg.setLastName("De Guidi")
sdg.displayData()

# imposto l'età della persona sdg

sdg.setAge(21)
sdg.displayData()

print("\n")

sdg.displayData()

print("\n")

print(f"{sdg.getName()}\n{sdg.getLastName()}\n{sdg.getAge()}")