# Scrivi una funzione contiene_parole(test, parole_chiave) che verifica se almeno una delle parole chiave è contenuta nel testo.
# parole_chiave è un set di parole.

def contiene_parole(testo:str, parole_chiave:set[str]) -> bool:

    for p in parole_chiave:

        if p in testo:

            return True
        
        else:

            return False
        
prova = contiene_parole("Ciao il mio nome è Francesco Totti", {"Ciao", "francesco"})
print(prova)