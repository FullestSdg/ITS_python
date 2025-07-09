'''
Scrivere una funzione seq_compresi(L,low,high) che restituisca il
 numero di valori nella lista L che sono compresi tra low e high
 (estremi inclusi). Potete assumere che gli argomenti siano di
 tipo corretto, cioè una lista di numeri e due numeri.
 Perciò non è necessario che verifichiate queste condizioni o che
 solleviate errori a riguardo.
 seq = [3,5,1,8,4,2,5,7,6,3,4,1,9,8,4]
 n = seq_compresi(seq,3,5)
 print(n)
'''

def seq_compresi(L:list[int], low:int ,high:int) -> int:

    numero_valori:list[int] = []

    for i in L:

        if i >= low and i <= high:

            numero_valori.append(i)
    
    return len(numero_valori)


seq = [3,5,1,8,4,2,5,7,6,3,4,1,9,8,4]
n = seq_compresi(seq,3,5)
print(n)
