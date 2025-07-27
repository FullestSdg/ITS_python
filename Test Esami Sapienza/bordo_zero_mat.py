'''
Scrivere una funzione bordo_zero_mat(M) che prenda come argo
mento una matrice rettangolare di dimensioni 𝑅×𝐶 con 𝑅 ≥ 1 e
 𝐶 ≥1, che restituisca True se il bordo della matrice è costituito
 esclusivamente da zeri, e che restituisca False altrimenti.
 Potete assumere che M sia una lista di liste, tutte della stessa
 lunghezza, e tutte contenenti numeri. Potete assumere che la
 matrice, così rappresentata, abbia almeno una riga e una colonna.
 Quindi non dovete verificare che l’argomento sia una matrice
 ben formata, e non dovete sollevare errori.
 M1 = [[0]]
 M2 = [[0,0,0,0], [0,7,8,0] , [0,0,0,0]]
 M3 = [[1,0,0], [0,8,0] , [0,2,-1], [0,0,0]]
 print(bordo_zero_mat(M1))
 print(bordo_zero_mat(M2))
 print(bordo_zero_mat(M3))
 1
 2
 3
 4
 5
 6
 True
 True
 False
 Il programma Python deve essere salvato nel file: bordo_zero_mat.py
'''
def bordo_zero_mat(M:list[list[int]]) -> bool:

    for i in M:

        if i[0] == 0:

            if i[-1] == 0:
                return True
        
        else:
            return False
M1 = [[0]]
M2 = [[0,0,0,0], [0,7,8,0] , [0,0,0,0]]
M3 = [[1,0,0], [0,8,0] , [0,2,-1], [0,0,0]]
print(bordo_zero_mat(M1))
print(bordo_zero_mat(M2))
print(bordo_zero_mat(M3))


'''
def bordo_zero_mat(M: list[list[int]]) -> bool:
    R = len(M)
    C = len(M[0])

    # Controlla prima riga
    if any(M[0][j] != 0 for j in range(C)):
        return False

    # Controlla ultima riga
    if any(M[-1][j] != 0 for j in range(C)):
        return False

    # Controlla le colonne esterne delle righe centrali
    for i in range(1, R - 1):
        if M[i][0] != 0 or M[i][-1] != 0:
            return False

    return True

'''


