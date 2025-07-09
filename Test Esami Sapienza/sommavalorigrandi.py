'''
Scrivete una funzione sommavalorigrandi(D,soglia) che accetti
 comeargomentoundizionarioeunvalorenumerico,echecalcoli
 la somma di tutti i valori corrispondenti ad una chiave del
 dizionario,chesianostrettamentemaggioridellasogliaindicata
 dasecondovalore.
 Adesempio:
 diz= {'xx': 44, 'yy':33, 'zz':22,'qw': 22, 'das': 11} 1
 print(sommavalorigrandi(diz,20)) 2
 print(sommavalorigrandi(diz,25)) 3
 print(sommavalorigrandi(diz,120)) 4
 121
 77
 0
 La funzionepuòassumere che il primoparametro diz sia un
 dizionariochefacorrispondereallechiavi solamentevalorinu
merici, eche il secondoparametrosoglia siaunvalorenume
rico. Pertantonondovete preoccuparvi di controllare queste
 condizioninellasoluzionedelvostroesercizio.
 IlprogrammaPythondeveesseresalvatonelfile: sommavalorigrandi.py
'''

def sommavalorigrandi(D:dict[str:int], soglia:int) -> int:

    somma = 0
    for values in D.values():

        if soglia <= values:
            somma += values

    return somma

diz = {'xx': 44, 'yy':33, 'zz':22,'qw': 22, 'das': 11} 
print(sommavalorigrandi(diz,20)) 
print(sommavalorigrandi(diz,25)) 
print(sommavalorigrandi(diz,120))

