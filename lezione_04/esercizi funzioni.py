#Esercizio 1
somma:int = 0
for i in range(20, 37+1):
    somma += i

print(f"La somma dei numeri da 20 a 37 è {somma}") 


somma2:int = 0
for i in range(1,10+1):
    somma2 += i

print(f"La somma dei numeri da 1 a 10 è {somma2}")


somma3:int = 0
for i in range(35,49+1):
    somma3 += i

print(f"La somma dei numeri da 35 a 49 è {somma3}")

#Esercizio 1 con le funzioni 

def somma(a:int,b:int):

    result:int = 0
    for i in range(a,b+1):
         result += i

    return result

print(f"La somma dei numeri da 1 a 15 è: {somma(1,15)} ")


def subtract(a:int, b:int):

    result = (a - b)

    return result

sottrazione = subtract(10,2)
print(f"La sottrazione è: {sottrazione}")