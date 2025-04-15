'''
Nel gioco del Blackjack, il valore di una mano è determinato dalla somma dei valori delle carte. Ogni carta ha un valore compreso tra 2 e 11 inclusi.

Il valore numerico delle carte (da 2 a 10) è equivalente al loro valore nominale.
Le figure (Jack, Regina, Re) non sono incluse in questo esercizio e vengono ignorate.
L'Asso (valore 11) può valere 1 o 11, a seconda di quale sia più favorevole al giocatore:
Se la somma della mano supera 21, e c'è almeno un asso valutato 11, quell'asso deve essere considerato 1 per evitare il "bust" (superare 21).
Scrivi una funzione che prende in input una lista di interi rappresentanti i valori delle carte e restituisce
il valore totale della mano secondo le regole del Blackjack.
'''

def blackjack_hand_total(cards: list[int]) -> int:

    somma_carte = 0
    asso = 1,11 #questo non serve

    for i in cards:

        somma_carte += i

        if i == 1 and somma_carte <= 10:
            asso == 11

        elif i == 11 and somma_carte > 21:
            somma_carte -= 10

        elif cards[1] == 11:
            somma_carte -= 5
        
    return somma_carte

risultato = blackjack_hand_total([1,11,10])
print(risultato)



def blackjack_hand_total(cards:list[int]) -> int:
    total:int = sum(cards)  # Calcola la somma iniziale dei valori delle carte
    num_aces:int = cards.count(11)  # Conta quanti assi (valore 11) sono presenti nella mano
    
    # Se il totale supera 21 e ci sono assi, riduci il valore degli assi a 1
    while total > 21 and num_aces > 0:
        total -= 10  # Cambia un asso da 11 a 1 per ridurre il totale
        num_aces -= 1  # Aggiorna il conteggio degli assi modificati
    
    return total  # Restituisce il valore totale della mano

# Test case
print(blackjack_hand_total([2, 3, 5]))  # Output: 10
print(blackjack_hand_total([10, 11]))   # Output: 21 (l'asso vale 11)
print(blackjack_hand_total([11, 8, 4])) # Output: 13 (l'asso diventa 1 per evitare il bust)
