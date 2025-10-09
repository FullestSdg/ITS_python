

def cronometro(fun): # decoratore (prende in input funzioni)
    
    def wrapper(*args): # innerfunction, questa funzione una volta che cronometro ha finito l'esecuzione viene persa a meno che non venga salvata in memoria

        import time 
        start = time.time()

        fun(*args)
        print(time.time() - start)

    return wrapper

@cronometro
def prova():
    print("ciao")

# def prova2():
#     print("Hello")


# prova = cronometro(prova) # questo sarebbe come scrivere @cronometro ecc
# prova2 = cronometro(prova2)

prova()
# prova2()

@cronometro
def somma(a:int, b:int):
    print(a+b)

somma(10,5)


def greeting(fun):

    def wrapper():

        print("Ciao come stai?")
        fun()

    return wrapper

@greeting
def francesco_totti():
    print("Potrei stare meglio\nForza Roma!!")

francesco_totti()




