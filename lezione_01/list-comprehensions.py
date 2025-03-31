lista_1 = [ i for i in range(10)]
dict_1 = { i : i for i in range (10)}

print(f"{lista_1}\n{dict_1}")


lista_2 = ["a", "b", "c"]
for idx, char in enumerate(lista_2):
    lista_2[idx] = char.upper()

print(lista_2)
