'''
6 Coppia con differenza minima (6 pun
ti)
 Scrivere una funzione coppia_differenza_minima(L) che riceva una
 lista L contentente solo numeri, e che restituisca una lista
 contenente le due posizioni [i,j] dove
 • i è minore di j;
 • L[i] e L[j] sono i due elementi della lista la cui differenza
 in valore assoluto è minima rispetto ad ogni altra coppia
 di elementi in L. La differenza minima può essere anche
 zero.
 Potete assumere che la lista L
 • contenga solo numeri;
 • abbia almeno due elementi;
 • la coppia a differenza minima sia unica.
 Pertanto non è necessario che verifichiate queste condizioni e
 che solleviate errori a riguardo.
'''

def coppia_differenza_minima(L:list[int]) -> list[int]:

    min_diff = float('inf')   
    pos_min = [0, 1]          

    for i in range(len(L)):

        for j in range(i + 1, len(L)):

            diff = abs(L[i] - L[j])

            if diff < min_diff:

                min_diff = diff
                pos_min = [i, j]

    return pos_min
    
seq = [-5,4,8,-3,1,3,10]
print(coppia_differenza_minima(seq))

