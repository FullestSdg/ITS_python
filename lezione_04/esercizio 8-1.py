# con input

def display_message(sentence:str) -> str:

    sentence:str = input("Inserire una frase: ")

    return sentence

mysentence = display_message("sentence")
print(mysentence)


# senza input

def display_message2(sentence2:str) -> str:

    return sentence2

mysentence2 = display_message2("Ciao sto imparando a fare le funzioni!")
print(mysentence2)