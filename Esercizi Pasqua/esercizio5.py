'''
Definire una funzione chiamata hypotenuse che calcoli la lunghezza dell'ipotenusa di un triangolo rettangolo.
La funzione deve ricevere due argomenti di tipo float (corrispondenti ai due lati del triangolo) e restituire l'ipotenusa come un float.

Per calcolare l'ipotenusa, si può ricorrere al teorema di Pitagora.
'''

def hypotenuse(numero1:float, numero2: float) -> float:

    ipotenusa = (numero1 ** 2 + numero2 ** 2) ** 0.5

    return ipotenusa

risultato = hypotenuse(3,4)
print(risultato)