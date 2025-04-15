def prime_factors(n: int) -> list[int]:
     
    fattori_primi:list[int] = []
    somma_fattori_primi = 0
    
    for i in range(2,n):
          
        resto = n % i

        if resto == 0 and somma_fattori_primi == n:
               
            fattori_primi.append(i)

        else:
               
            continue
          
    return fattori_primi


def prime_factors(n: int) -> list[int]:

    divisori:list[int] = []
    i = 2
    
    while i <= n:
        
        if n % i == 0:
            
            divisori.append(i)

            n = n // i
        
        else:
            i += 1

    return divisori




risultato = prime_factors(4)
print(risultato)