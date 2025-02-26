#Esercizio n.7
a:list = [1,2,3,4,5]
b:list = [15,22,18,50,100]
c:list = []

for x, y in zip(a,b[::-1]):
    c.append(x + y)
print(f"La somma incrociata è: {c}")
print(f"{a}\n{b}\n{c}\n")