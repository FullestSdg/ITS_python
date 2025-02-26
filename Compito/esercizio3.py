#Esercizio n.3
stringa: str = input("Inserisci una frase: ")
lunghezza_stringa = len(stringa) - 1
stringa_invertita = ""

for i in range (len(stringa)):
    stringa_invertita += stringa[lunghezza_stringa]
    lunghezza_stringa = lunghezza_stringa - 1
print(stringa_invertita)    



