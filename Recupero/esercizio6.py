lista1:list[int] = []

for i in range(2,14+1,2):
    
    lista1.append(i)

lista2:list[int] = []

for i in range(1,13+1,3):

    lista2.append(i)

lista3:list[int] = []

for i in range(30, 0-1, -5):

    lista3.append(i)


lista4:list[int] = []

for i in range(5,45+1, 10):

    lista4.append(i)

print(f"{lista1}\n{lista2}\n{lista3}\n{lista4}")
print(f"\n")
print([x for x in range(2,14+1,2)])

print([x for x in range(1,13+1,3)])

print([x for x in range(30, 0-1, -5)])

print([x for x in range(5,45+1, 10)])
