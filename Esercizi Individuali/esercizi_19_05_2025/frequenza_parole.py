'''
2. Frequenza delle parole
Data una stringa, conta quante volte appare ciascuna parola.
'''

testo = "ciao come stai ciao tutto bene"
# crea un dizionario con le frequenze delle parole

parole:list[str] = ["ciao", "come", "stai", "ciao", "tutto", "bene"]

for p in parole:

    frequenza_parole = 0

    if p:
        
        frequenza_parole += 1

        frequenza_parole_dizionario:dict[str : int] = {}

        frequenza_parole_dizionario[p] = frequenza_parole

        print(frequenza_parole_dizionario)