from random import randint
from Rep3_S_DeGuidi import IntGTZ

lista_numeri:list[IntGTZ] = []
lista_numeri_duplicati:list[IntGTZ] = []

for n in range(0,15+1):

    n = randint(1,100)

    lista_numeri_duplicati.append(n)

    if n not in lista_numeri:
                 
        lista_numeri.append(n)

numeri = lista_numeri
print(numeri)