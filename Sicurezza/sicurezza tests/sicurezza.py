'''
Scrivere un programma PYTHON che a partire da una stringa la cifra con la tecnica XOR
Successivamente mostrare che la stringa cifrata, riapplicando lo stesso XOR, torna la stringa originale
Per fare lo XOR utilizzate un solo valore: 57
Quindi data la stringa di esempio “Nel mezzo del cammin di nostra vita”, dovete fare per ogni carattere della stringa lo xor con il valore 57
“N” xor 57, “e” xor 57, …
Ottenendo una lista di numeri es: 78 (che è il codice asciii  della lettera N) xor (si indica con il simbolo ^) => 78 ^ 57 = 119
E così via per tutta la stringa.
Al termine stampare la lista di numeri ottenuti
In fondo a partire dalla lista di numeri, riapplicare lo xor sempre con 57 e quindi ottenere (ricostruendola) la stringa originale
NB: potreste utilizzare input(“…”) in modo da leggere sia la stringa da cifrare, sia il valore segreto da applicare come xor
'''



parola:str = input("Inserisci una frase: ")
valore_segreto:int = int(input("Inserisci un valore segreto: "))

lista_numeri_cifrati:list[int] = []

# VERSIONE BRUTTA BLEAH 🤮
'''
for letters in parola:

    new_letter = ord(letters) ^ valore_segreto

    lista_numeri_cifrati.append(new_letter)

print(lista_numeri_cifrati)

stringa2 = "" 

for numbers in lista_numeri_cifrati:

    new_value = numbers ^ valore_segreto

    stringa2 += chr(new_value)

print(stringa2)
'''

# VERSIONE BELLA 😎

print("".join([chr(number ^ valore_segreto) for number in [ord(letter) ^ valore_segreto for letter in parola]]))




    
