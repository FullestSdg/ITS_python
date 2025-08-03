'''
🔵 Esercizio 1 – Conta vocali
Scrivi una funzione conta_vocali(stringa) che prende una stringa in input e restituisce il numero totale di vocali presenti (a, e, i, o, u – sia maiuscole che minuscole).
'''

def conta_vocali(parola:str) -> dict[str : int]:

    vocali:list[str] = ["a", "e", "i", "o", "u"]
    frequenza_a = 0
    frequenza_e = 0
    frequenza_i = 0
    frequenza_o = 0
    frequenza_u = 0

    for p in parola.lower():
        match p:

            case p if p in vocali and p == "a":
                frequenza_a += 1
            
            case p if p in vocali and p == "e":
                frequenza_e += 1

            case p if p in vocali and p == "i":
                frequenza_i += 1

            case p if p in vocali and p == "o":
                frequenza_o += 1
            
            case p if p in vocali and p == "u":
                frequenza_u += 1

    return {"a": frequenza_a, "e": frequenza_e, "i": frequenza_i,"o": frequenza_o, "u": frequenza_u}

print(conta_vocali("Giuseppe Ungaretti si è fatto la cacca nei pantALONI"))

            

