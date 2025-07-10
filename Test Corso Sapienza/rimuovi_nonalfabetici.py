'''
Sostituzione dei caratteri non alfabetici
Scrivere una funzione rimuovi_nonalfabetici(frase) che data una stringa
di caratteri restituisce una nuova stringa di caratteri. La nuova stringa deve
essere una modifica di frase, dove ogni carattere non alfabetico deve essere
sostituito da uno spazio. Ad esempio, se il parametro è la stringa
"Buongiorno, vengo dall'Umbria."
deve essere restituita la stringa
"Buongiorno  vengo dall Umbria "
Notare la presenza di un elemento " " in corrispondenza dei caratteri virgola,
apostrofo e punto.
Per verificare se un carattere contenuto in una variabile, per esempio di nome
pippo, è una lettera si può usare il metodo pippo.isalpha(), che restituisce
True oppure False.
Il programma Python deve essere salvato nel file: rimuovi_nonalfabetici.py

'''

def rimuovi_nonalfabetici(frase: str) -> str:

    nuova_frase = ""
    
    for char in frase:

        if char.isalpha():
            nuova_frase += char

        else:
            nuova_frase += " "

    return nuova_frase

print(rimuovi_nonalfabetici("Buongiorno, vengo dall'Umbria."))


