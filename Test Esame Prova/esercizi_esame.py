# def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    
#     tuples_dict = {}
#     list_value = []
    
#     for tuple in tuples:
        
#         if tuple[0] not in tuples_dict:
            
#             tuples_dict[tuple[0]] = list_value 

#             list_value.append(tuple)
            
#         else:
#             tuples_dict[tuple[0]] = list_value.append(tuple[1])
    
#     return tuples_dict

# print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))



# def classifica_numeri(lista: list[int]) -> dict[str:list[int]]:

#     lista_pari = []
#     lista_dispari = []
#     dict_pari = {}
#     dict_dispari = {}

#     for n in lista:

#         if n % 2 == 0:

#             lista_pari.append(n)
#             dict_pari["pari"] = lista_pari

#         else:
#             lista_dispari.append(n) 
#             dict_dispari["dispari"] = lista_dispari

#     return dict_pari | dict_dispari


# print(classifica_numeri([1, 2, 3, 4, 5, 6]))

import math
from typing import *


def string_counter(words:list[str]) -> dict[str,int]:

    counter:dict[str,int] = {}
    caratteri:str = "abcdefghijklmnopqrstuvwyz"
    parola_pulita:str = " "

    for word in words:

        modified_word = word.lower()

        modified_word2 = modified_word.strip("!,.:?'''")

        parola_pulita2 = modified_word2.split()

        for letters in modified_word:
            
            if letters in caratteri:

                parola_pulita += letters    

        for p in parola_pulita2:
                
            if p not in counter:
                counter[p] = 1 

            else:
                counter[p] += 1

    return counter 


print(string_counter(["ciao", "ciao so,no giovanni!"]))



def check_min_max(numbers:list[int]) -> tuple[int, int]:

    max:float = numbers[0]
    min:float = numbers[0]

    for n in numbers:

        if n >= max:

            new_max = n 
        
        elif n <= min:

            new_min = n 
    
    return (new_max, new_min)



print(check_min_max([10,5,2,7,9,-12]))


def ordered_list(numbers:list[int]) -> list[int]:

    pass



print(ordered_list([9,6,4,2,10]))




def findtheelement(lista:list[Any], element:Any) -> Any:

    for elements in lista:

        if elements == element:

            return f"Elemento trovato nella lista: {element}"

    return f"Elemento {element} non trovato"

print(findtheelement(["ciao", 12, {"francesco" : 65}, 6.5, True], 12))






