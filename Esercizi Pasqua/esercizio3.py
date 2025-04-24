'''
Sviluppare una funzione in Python per calcolare lo stipendio lordo di ciascuno dei diversi impiegati.
L'azienda paga 10 dollari all'ora per le prime 40 ore di lavoro e paga "una volta e mezza" la paga oraria per tutte le ore di lavoro oltre le
40 ore.
 
Per ogni operaio, viene fornito il numero di ore che tale impiegato ha lavorato durante la settimana.
La vostra funzione deve ricevere questa informazione per ogni impiegato e determinare e stampare lo stipendio lordo.
'''

def calcola_stipendio(ore_lavorate: int) -> float:
    stipendio:float = 0
    differenza_ore:float = 0

    if ore_lavorate <= 40:
        stipendio = ore_lavorate * 10
    
    else:
        differenza_ore = ore_lavorate - 40
        stipendio = (ore_lavorate * 10) + differenza_ore * 5
        
         

    return stipendio

risultato = calcola_stipendio(40)
risultato1 = calcola_stipendio(45)
print(f"{risultato}\n{risultato1}")