# Ciclo while
'''i = 1
max:float = float(input("Inserire un numero: "))

while i < 4:
    n:float = float(input("Inserire un numero: "))
    i += 1

    if n > max:
        max = n
    
    else:
        continue

print(max)
'''
# Repeat

'''i = 1
max:float = float(input("Inserire un numero: "))

while True:
    i += 1
    n:float = float(input("Inserire un numero: "))

    if n > max:
        max = n 

    if i == 4:
        break

print(max)
'''
# Ciclo for

max:float = float(input("Inserire un numero: "))

for i in range(3):

    n:float = float(input("Inserire un numero: "))
    if n > max:
        max = n

print(max)