def moltiplicazione(lista_numeri:list[int], threshold:int) -> int:
    prodotto = 1
    for numeri in lista_numeri:

        if numeri < threshold:

            prodotto *= numeri

    return prodotto

print(moltiplicazione([1,2,3,4], 4))