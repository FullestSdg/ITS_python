'''
2. Guess the Number Game:

Create a function that generates a random number within a range specified by the user.
Prompt the user to guess the number within a specified maximum number of attempts.
Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.
'''
from random import *

def GuessTheNumber() -> str:

    range1:int = int(input("Inserisci il range minimo del numero casuale: "))
    range2:int = int(input("Inserisci il range massimo del numero casuale: "))

    if range1 > range2:
        raise ValueError(f"Il primo numero inserito non può essere maggiore del secondo numero inserito")
    
    tentativi:int = int(input("Inserisci il numero di tentativi massimi per indovinare: "))

    if tentativi == 0:
        raise ValueError("I tentativi non possono essere 0")
    
    soluzione = randint(range1,range2)
    contatore = 0

    while True:

        try:
            guess = int(input("Inserisci il tuo tentativo: "))

        except ValueError:
            print("Inserisci un numero valido.")
            continue

        if guess == soluzione:
            contatore += 1
            break
             
        elif guess > soluzione:
            contatore += 1
            print("❌ Numero troppo alto!")
            print(f"Tentativi rimasti: {tentativi - contatore}")

        else:
            contatore += 1
            print("❌ Numero troppo basso!")
            print(f"Tentativi rimasti: {tentativi - contatore}")
    
        if contatore == tentativi:
            break

    if contatore == tentativi and guess != soluzione:
        return f"💀 Tentativi terminati, mi spiace ma non hai indovinato il numero: {soluzione}"
    else:
        return f"🎉 Congratulazioni hai indovinato il numero! ({soluzione})\nTentativi usati: {contatore}"
            

print(GuessTheNumber())

