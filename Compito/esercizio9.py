#Esercizio 9 
pigreco_approssimato:list = [3.14, 3.141, 3.1415, 3.14159]
pigrego_risultato:list = {}
pi:int = 4
i:int = 1
termini_necessari:int = 1

while len(pigrego_risultato) < len(pigreco_approssimato):
    
    if i % 2 == 0:
        pi += 4 / (i * 2 + 1)
    
    else:
        pi -= 4 / (i * 2 + 1)

    for v in pigreco_approssimato: # v = valore
        
        if v not in pigrego_risultato: # v = valore
            
            if pi > v and pi - v < 0.00001:
                pigrego_risultato[v] = termini_necessari
            
            elif pi < v and v - pi < 0.00001:
                pigrego_risultato[v] = termini_necessari
    i += 1
    termini_necessari += 1

for v in pigrego_risultato: # v = valore
    print(f"π = {v}, {pigrego_risultato[v]} termini.")