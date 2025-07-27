'''
 Scrivereunafunzione riga_max_file(nomefile) che ricevacome
 argomentoilnomediunfileditestocontenenteinciascunariga
 unaseriedi interi separatidaspazio, erestituiscalaposizione
 della rigaconsommamassima. Leposizioni di riga si devono
 contareapartireda0. Nelcasodipiùrigheconsommamassima
 deveessererestituitalaposizionedellaprimaditali righe.
 Si assuma che il file contenga almeno una riga, e che tutte
 le righe contengano esclusivamente interi (positivi o negati
vi) separati da spazi. Ilprogrammanondevenecessariamente
 occuparsidicontrollarequestecondizioni.
 Nel casosi voglia leggeretutto il file inuna solaoperazione
 .read()si consigliadi spezzarelastringainsingolerighecon
 ilmetodo.splitlines()
 Adesempiosulfileriga_max_file2.txtcontenente
 20 1-45
 61710-9 1
 24 55 0
 234-2
 si dovrà restituire il valore1, poiché ledue righeconsomma
 massima,paria25, sonolariga1elariga3
 print(riga_max_file('riga_max_file2.txt'))
'''

def riga_max_file(nomefile:str) -> int:

    pass