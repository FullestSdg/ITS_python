from mytypes_azienda1 import *
from datetime import date
from impiegato import Impiegato
from dipartimento import Dipartimento
from progetto import Progetto
from coinvolto import Coinvolto
from datetime import timedelta

'''
tel1: Telefono = Telefono("3334445566")
tel2: Telefono = Telefono("3337778899")
ind: Indirizzo = Indirizzo("Viale Cesare Pavese", "205b",
                           CAP("00144"))

alice: Impiegato = Impiegato("Alice", "Alessi",
                             date(year=1990, month=12, day=31),
                             RealGEZ(18000))
print(f"Ho creato l'impiegata {alice.nome()} {alice.cognome()}")

bob: Impiegato = Impiegato("Bob", "Burnham",
                             date(year=1997, month=10, day=11),
                             RealGEZ(19000))
print(f"Ho creato l'impiegato {bob.nome()} {bob.cognome()}")


dip1: Dipartimento = Dipartimento("Vendite", tel1, ind)

print(f"Ho creato il dipartimento {dip1}")


dip2: Dipartimento = Dipartimento("Acquisti", tel2, None)
print(f"Ho creato il dipartimento {dip2}")

t: frozenset[Telefono] = dip1.telefoni()

print("dip1.telefoni() = " + str(dip1.telefoni()))

dip1.add_telefono(Telefono("3481265413"))

print("dip1.telefoni() = " + str(dip1.telefoni()))
'''

alice = Impiegato("Alice", "Meraviglia", date(year=2004,month=2, day=12), 0)
pegaso = Progetto("Pegaso", 5678.67)
biagio = Impiegato("Biagio", "Federici", date(year=1999,month=7, day=24), 1800)
totti = Impiegato("Francesco", "Totti", date(year=1976,month=9, day=27), 1000000)


domani = date.today() + timedelta(hours=24)
print(domani)
print(f"")

pegaso.add_impiegato(alice, date.today())
pegaso.add_impiegato(biagio, domani)
pegaso.add_impiegato(totti, date.today())

print(pegaso.lista_impiegati)

print(pegaso.iscoinvolto(alice))
print(pegaso.iscoinvolto(biagio))

pegaso.remove_impiegato(totti)
pegaso.remove_impiegato(biagio)
# pegaso.remove_impiegato(alice)

print(pegaso.iscoinvolto(totti))

print(pegaso.check_ultimo_impiegato())

# pegaso.remove_impiegato(totti) #     da errore :(


