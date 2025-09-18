from dottore import * 
from persona import * 
from fatture import *
from paziente import *

# -------------------------------
# Codice Driver come da traccia
# -------------------------------

# Creiamo 3 pazienti per la prima lista e 1 per la seconda
paz1 = Paziente("Mario", "Rossi", "ID001")
paz2 = Paziente("Anna", "Verdi", "ID002")
paz3 = Paziente("Luca", "Bianchi", "ID003")

paz4 = Paziente("Giulia", "Neri", "ID004")

lista_pazienti1 = [paz1, paz2, paz3]  # 3 pazienti
lista_pazienti2 = [paz4]              # 1 paziente

# Creiamo due dottori
dottore1 = Dottore("Giovanni", "Ferrari", "Cardiologo", 150.0)
dottore2 = Dottore("Alessandro", "Moretti", "Neurologo", 200.0)

# Impostiamo l'età di ogni medico affinché risultino validi (>30 anni)
dottore1.setAge(45)
dottore2.setAge(52)

# I due medici si presentano
print("\n-- Presentazione medici --")
dottore1.doctorGreet()
dottore2.doctorGreet()

# Creiamo le fatture
fattura1 = Fattura(lista_pazienti1, dottore1)
fattura2 = Fattura(lista_pazienti2, dottore2)

# Stampiamo il salario di ogni singolo dottore
salario_d1 = fattura1.getSalary()
salario_d2 = fattura2.getSalary()

print(f"\nSalario Dottore1: {salario_d1} euro!")
print(f"Salario Dottore2: {salario_d2} euro!")

# Rimuoviamo un paziente dal dottore1 e lo aggiungiamo al dottore2
print("\n-- Trasferimento paziente --")
paziente_trasferito = fattura1.removePatient("ID002")
if paziente_trasferito is not None:
    fattura2.addPatient(paziente_trasferito)

# Stampiamo i salari dopo il trasferimento
salario_d1_after = fattura1.getSalary()
salario_d2_after = fattura2.getSalary()

print(f"\nSalario Dottore1 dopo trasferimento: {salario_d1_after} euro!")
print(f"Salario Dottore2 dopo trasferimento: {salario_d2_after} euro!")

# Guadagno totale ospedale
guadagno_totale = salario_d1_after + salario_d2_after
print(f"\nIn totale, l'ospedale ha incassato: {guadagno_totale} euro!")