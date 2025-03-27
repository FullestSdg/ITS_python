'''def calculate_average(numbers: list[int]) -> float:

    somma = 0
    media = 0

    if len(numbers) == 0:
        return len(numbers)
    else:
        for n in numbers:
            somma += n
            media = somma / len(numbers)
        return media

list1:list[int] = []
result = calculate_average(list1)
print(result)
'''

'''def sum_above_threshold(numbers: list[int], threshold:int = None) -> int:
    # prima cancella ... e definisci parametro e tipo per il dato mancante
    # successivamente cancella pass e scrivi il tuo codice
    somma = 0

    for n in numbers:

        if n > threshold:
            somma += n
    
    return somma

list2:list[int] = [15,2,10,25,30]
risultato = sum_above_threshold(list2, 76)
print(risultato)'
'''

'''def rounded_average(numbers: list[int]) -> int:
    # cancella pass e scrivi il tuo codice
    somma = 0

    if len(numbers) == 0:

        return len(numbers)

    else:
        for n in numbers:
           somma += n
           media = somma / len(numbers)

        return round(media)

numbers:list[int] = [1,1,2,2]
risultato = rounded_average(numbers)
print(risultato)
'''
'''
def countdown(n: int) -> int:
    # cancella pass e scrivi il tuo codice
    count = -1

    while n > count:
        n -= 1
        print(n+1)

countdown(7)

def countdown2(n:int) -> int:

    while n >= 0:
        
        print(n)
        n -= 1
    

countdown2(8)'
'''
'''
def check_parentheses(expression: str) -> bool:
    
    count_parentesi = 0

    for parentesi in expression:

        if parentesi == "(":
            count_parentesi += 1
        
        elif parentesi == ")":
            count_parentesi -= 1
    
    if count_parentesi > 0:
        return False
    
    if count_parentesi == 0:
        return True


frase = check_parentheses("ciao ()francesco,)(mi chiamo giuseppe roberto (sono napoletano)")
print(frase)
'''
'''
def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:

    for n in elements_to_remove:

        if n in original_set:
            original_set.remove(n)
    
    return original_set

risultato = remove_elements({2,3,4}, [1,2,5])
print(risultato)
'''

'''def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    # cancella pass e scrivi il tuo codice
    

risultato = merge_dictionaries({"x": 5}, {"x": 10})
print(risultato)
'''

'''def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    # cancella pass e scrivi il tuo codice
    if conditionA == True or conditionB and conditionC == True:

        return "Operazione permessa"
    
    else:

        return "Operazione negata"
'''



    
    
