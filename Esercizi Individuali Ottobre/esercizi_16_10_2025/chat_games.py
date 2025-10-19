import random 

def StorpiatoreParole(parola:str) -> str:

    if isinstance(parola, str):

        letters = []
        new_parola = ""

        for lettera in parola:
            letters.append(lettera)

        if len(letters) == len(parola):

            while len(letters) != 0:

                lettera_casuale = random.choice(letters) 
                new_parola += lettera_casuale
                letters.remove(lettera_casuale)

    else:
        return f"Parola inserita non valida!\n{parola} non è una st ringa!"
    
    return new_parola

print(StorpiatoreParole("ciao"))   


def StorpiatoreParole2(parola:str) -> str:

    if not isinstance(parola, str) or not parola:
        return f"Parola inserita non corretta: {parola}"
    
    else:
        return "".join(random.sample(parola, len(parola)))

print(StorpiatoreParole2("rubinetto"))



