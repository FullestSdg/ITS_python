parola = input("Inserisci una parola: ")
chiave_segreta = int(input("Inserisci una chiave segreta: "))
lista_numeri_cifrati = []

for letters in parola:

    new_letter = ord(letters) ^ chiave_segreta

    lista_numeri_cifrati.append(new_letter)

print(lista_numeri_cifrati)

decifra = " "

for numbers in lista_numeri_cifrati:

    new_value = numbers ^ chiave_segreta

    decifra += chr(new_value)

print(decifra)

print("".join([chr(number ^ chiave_segreta) for number in [ord(letter) ^ chiave_segreta for letter in parola]]))