from persona import Persona

from studente import Studente 

# creo un oggetto p della classe persona

p:Persona = Persona("Sergio", "De Guidi", 21)

# visualizzare le informazioni dell'oggetto p
print(p)

# creare un oggetto studente1 della classe Studente

studente1:Studente = Studente("Mario", "Rossi", 20, "012245") 

# visualizzare le informazioni relative all'oggetto studente1
print(studente1)

# controllare se studente1 è istanza della classe Studente.
# isinstance(obj), Class -> controllare se l'oggetto obj sia istanza della classe Class
# in caso affermativo -> True
# in caso negativo -> False

if isinstance(studente1, Studente):
    print("studente1 è istanza della classe Studente")

# controllo se studente1 sia anche una un'istanza della classe Persona

if isinstance(studente1, Persona):
    print("studente1 è istanza della classe Studente ma è anche istanza della classe Persona")

# controllo se l'oggetto p sia una istanza della classe Persona

if isinstance(p, Persona):
    print("p è un oggetto della classe Persona")

# controllare se l'oggetto p sia anche un'istanze della classe Studente 

if isinstance(p, Studente):
    print("p è un oggetto della classe Persona, ma è anche un oggetto della classe Studente")

else:
    print("p è un oggetto della classe Persona, ma non è un oggetto della classe Studente")

# come controllare se una classe è sottoclasse di un'altra
# controllo se la classe Studente è una sottoclasse di Persona
# issubClass(Class1, Class2) -> controlla se la classe Class1 è sottoclasse della classe Class2
# in caso affermativo -> True
# in caso negativo -> False

if issubclass(Studente, Persona):
    print("la classe Studente è sottoclasse della classe Persona")