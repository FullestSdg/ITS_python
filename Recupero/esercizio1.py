from typing import Any

def convertitore(lista_tuple:list[tuple[Any,Any]]) -> dict:

    new_dict:dict = {}

    for tuple in lista_tuple:

        if tuple[0] in new_dict:

            new_dict[tuple[0]] += tuple[1]

        else:
            
            new_dict[tuple[0]] = tuple[1]

    return new_dict


print(convertitore([("ciao12", "alberto"), ("giovanni", "francesco"), ("ciao", 10), ("ciao", 10 )]))

