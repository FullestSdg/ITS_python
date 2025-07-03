

def recursivePalindrome(parola:str) -> bool:

    parola1 = parola.lower().replace(" ", "")

    if not parola1:

        return True

    elif parola1[0] != parola1[-1]:
       
        return False 
        
    else:
        parola1[0] == parola1[-1]

        return recursivePalindrome(parola1[1:-1])


print(recursivePalindrome("i TopI nOn AvevaNo NIPOtI"))



while True:

    nome:str = input("Inserisci un nome: ")

    lista_nomi:str = []

    if nome not in lista_nomi:

        lista_nomi.append(nome)

        if len(lista_nomi) > 30:
            break
    
    else:
        break 

    for nomi in lista_nomi:

        if len(nomi) > len(nomi):

            lista_nome_più_lungo = []

            lista_nome_più_lungo.append(nomi)

            print(lista_nome_più_lungo[-1])

    


        

