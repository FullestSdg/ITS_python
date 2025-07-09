def convertitore(lista_numeri:list[int|float]) -> dict[str, list[int|float]]:

    new_dict:dict = {}
    lista_positivi:list = []
    lista_negativi:list = []

    for numeri in lista_numeri:

        if numeri >= 0:

            lista_positivi.append(numeri)

            new_dict["Positivi"] = lista_positivi

        else:

            lista_negativi.append(numeri)

            new_dict["Negativi"] = lista_negativi

    return new_dict


print(convertitore([1,2.5,3,-4,5,6,-2,-5,-2.5]))