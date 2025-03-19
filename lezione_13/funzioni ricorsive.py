'''def countdown(n:int) -> None:

    if n >= 0:
       
       while n >= 0:
          
          print(n)
          n -= 1

    else:
       print("Errore, numero inserito non valido")
               
countdown(5)
countdown(-5)
'''

# Funzioni Ricorsive

'''def countdown(n:int) -> None: 

    if n < 0:
        print("Errore, il numero inserito è negativo ")

    elif n == 0:
        print(0)

    else:
        print(n)
        countdown(n-1)

countdown(5)
'''

'''def sum(n:int) -> int:

    if n < 0:
        print("Errore numero inserito negativo")
        
        return None
    
    else:
        sum:int = 0

        while n:

            sum += n
            n -= 1

        return int(sum)

somma = sum(5)
print(somma)
'''

'''
def RecursiveSum(n:int) -> int:

    if n < 0:

        print("Errore numero inserito negativo")
        return None
    
    elif n == 0:

        return 0

    else:
        
        return int(n + RecursiveSum(n-1))
    
print(RecursiveSum(5))
'''

'''def sumInRange(a:int, b:int) -> int:

    if a > b:

        c = a # c = variabile temporanea

        a = b
        b = c
    
    sum = 0
    while b >= a:

        sum += b
        b -= 1

    return sum

somma = sumInRange(5,10)
print(somma)

somma = sumInRange(10,5)
print(somma)
'''

'''def RecursivesumInRange(a:int, b:int) -> int:

    if a > b:

        c = a # c = variabile temporanea

        a = b
        b = c
    
    if b == a:

        return int(a)
    
    else:

        return int (b + RecursivesumInRange(a, b -1))
    
print(RecursivesumInRange(5,10))
print(RecursivesumInRange(10,5))'
'''

def fibonacci(n:int) -> int:

    if n <= 0:
        
        return 0
    
    elif n == 1:

        return 1
    
    else:
        
        return int (fibonacci(n-1) + fibonacci(n-2))
    
print(fibonacci(6))