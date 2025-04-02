# Safe Square Root: Write a function safe_sqrt(number) that calculates the square root of a number using math.sqrt().
#  Handle ValueError if the input is negative by returning an informative message.
import math

def safe_qrt(number:int):

    if number < 0:
        raise ValueError("Numero inserito in negativo, non è possibile fare la radice quadrata")
    
    result = math.sqrt(number)

    return result

radice_quadrata = safe_qrt(25)
print(radice_quadrata)

radice_quadrata_negativa = safe_qrt(-25)
print(radice_quadrata_negativa)