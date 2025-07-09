

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


nomi:set[str] = set()

while True:

    nome = input("Insersci un nome: ").strip()

    if nome == "":

        print("Errore: il nome non può essere vuoto.")
        
        continue
    if len(nome) >= 20:

        print("Errore: il nome deve essere più corto di 20 caratteri.")

        continue

    if nome in nomi:

        break

    nomi.add(nome)

    if len(nomi) == 30:
        break

if nomi:

    nome_piu_lungo = max(nomi, key=len)

    print(f"\nHai inserito {len(nomi)} nomi distinti.")

    print(f"Il più lungo è {nome_piu_lungo} con {len(nome_piu_lungo)} caratteri.")
else:
    
    print("\nNon è stato inserito alcun nome valido.")


    


        

