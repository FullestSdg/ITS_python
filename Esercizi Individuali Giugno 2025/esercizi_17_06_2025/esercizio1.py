'''
Sistema di Gestione Biblioteca
Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli e visualizzare quali libri sono disponibili in un dato momento.
 
Classi:
- Libro: Rappresenta un libro con titolo, autore, stato del prestito. Il libro deve essere inizialmente disponibile (non prestato).

- Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

    Metodi della classe:
    - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.

    - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. Se non ci sono libri disponibili, restituisce un messaggio di errore.
    '''

class Libro:

    def __init__(self, titolo:str, autore:str, stato_prestito=False) -> None:

        self._titolo = titolo 
        self._autore = autore 
        self._stato_prestito = stato_prestito

    def __repr__(self) -> str:
        return f"Libro -> Titolo: {self._titolo} Autore: {self._autore}"

class Biblioteca(Libro): 

    def __init__(self) -> None:

        self._catalog:list[Libro] = []

    def aggiungi_libro(self, libro:Libro) -> str:

        if libro not in self._catalog:

            self._catalog.append(libro)

            return f"{libro} è stato aggiunto con successo al catalogo dei libri!"
        
        else:
            return f"Non è stato possibile aggiungere {libro} al catalogo, in quanto già presente!"
        
    def presta_libro(self, titolo:str) -> str:

            for libro in self._catalog:

                if libro(self._titolo) == titolo and libro(self._stato_prestito) == False:

                    libro(self._stato_prestito) == True 

                    return f"{titolo} prestato con successo!"


ciao:Biblioteca = Biblioteca()
libro:Libro = Libro("Moby Dick", "Giuseppe")
libro2:Libro = Libro("Moby Dick", "Giuseppe")

print(libro._titolo)

print(ciao.aggiungi_libro(libro))

print(ciao.aggiungi_libro(libro2))

print(ciao._catalog)



