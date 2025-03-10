nome:str = input("Inserisci un nome: ")
vendite:int = int(input("Inserisci il numero delle vendite: "))

max_nome:str = nome
max:int = vendite
min_nome:str = nome
min :int= vendite

contatore = 0

for contatore in range(19):
    
    new_nome:str = input("Inserisce un nuovo nome: ")
    new_vendite:int = int(input("Inserisci un nuovo numero delle vendite: "))

    if new_vendite > max_vendite:
        max_nome = new_nome
        max_vendite = new_vendite

    elif new_vendite < max_vendite:
        min_nome = new_nome
        min_vendite = new_vendite 

print(f"Il venditore con più vendite è: {max_nome} con {max_vendite} vendite")
