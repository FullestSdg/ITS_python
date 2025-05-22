'''
2. Frequenza delle parole
Data una stringa, conta quante volte appare ciascuna parola.
'''

testo = "ciao come stai ciao tutto bene"
# crea un dizionario con le frequenze delle parole

parole = testo.split()
frequenze = {}

for parola in parole:

    if parola in frequenze:
    
        frequenze[parola] += 1

    else:
    
        frequenze[parola] = 1

print(frequenze)
