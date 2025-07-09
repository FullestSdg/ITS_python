lista1:list[int] = [1,2,3,4,5]

def printListBackward(lista:list[int]) -> None:

    if not lista:
        print(" ")
    
    else:
        print(lista[-1])

        printListBackward(lista[:-1])

print(printListBackward(lista1))

        