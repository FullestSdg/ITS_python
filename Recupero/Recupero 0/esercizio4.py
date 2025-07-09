def condizione(x:bool, y:bool, z:bool) -> str:

    if x == True and (y == True or z == True):

        return "Azione Permessa"
    
    else:

        return "Azione Negata"
    
print(condizione(True, False, True))
print(condizione(False, True, True))