# CIFRARIO DI CESARE

from string import ascii_lowercase

frase:str = "flavio"

def cifrario(frase:str, chiave:int) -> str:

    # Stringa che conterrà il risultato

    risultato:str = ""

    # Voglio trovare l'indice corrispondente al carattere corrente Esempio carattere="a" idx = 0
    # perchè ascii_lowercase = ["a", "b", "c", ...]

    for carattere in frase:

        idx:int = ascii_lowercase.index(carattere)

        idx = (idx + chiave) % len(ascii_lowercase)

        risultato += ascii_lowercase[idx]

    return risultato

print(cifrario(frase, 2))
                                     

