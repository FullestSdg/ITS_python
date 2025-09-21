from film import Film
from movie_genre import *

### CLASSE: Noleggio
'''In un file "noleggio.py", creare una classe Noleggio.
Questa classe deve avere come attributi una lista di film contenuti in negozio (film_list), un dizionario (rented_film) che ha come chiave un numero intero rappresentante l'id del cliente che ha affittato il film e per valore una lista contenente i film affittati dal cliente.
 
- Definire i seguenti metodi:
init(film_list): tale metodo, inoltre,  deve creare un dizionario vuoto chiamato rented_film.

isAvaible(film): tale metodo deve ritornare True se il film passato come argomento è presente nell'inventario del negozio, false in caso contrario. Se il film è disponibile in negozio stampare: "Il film scelto  è disponibile: {titolo_film}!". Se il film non è disponibile in negozio stampare: "Il film scelto  non è disponibile: {titolo_film}!".

rentAMovie(film, clientID): tale metodo deve gestire il noleggio di un film ed ha come argomenti il film da noleggiare ed il codice id del cliente che lo noleggia. Affinché sia possibile noleggiare un film, un film deve essere disponibile in negozio. Pertanto, il metodo deve verificare la disponibilità. Nel caso in cui il film richiesto sia disponibile, rimuoverlo dalla lista dei film disponibili in negozio, poi riempire il dizionario rented_film in questo modo:
la chiave sarà l'id del cliente che noleggia (id_client)
il corrispondente valore sarà una lista contenente i film noleggiati da quel cliente.
Pertanto, il film noleggiato, una volta rimosso dalla lista dei film disponibili in negozio deve essere aggiunto alla lista dei film noleggiati dal cliente dato.  Se il cliente ha potuto noleggiare il film richiesto, stampare: "Il cliente {clientId} ha noleggiato {titolo_film}!". Se, invece, il film richiesto non è disponibile pe il noleggio, stampare: Non è possibile nolegiare il film {titolo_film}!".

giveBack(film, clientID, days): questo metodo consente di restituire un film noleggiato in negozio, ed ha come argomenti il film da restituire, il codice ID del client che restituisce il film, il numero dei giorni in cui il cliente ha tenuto il film per se.  Il film da restituire deve essere rimosso dalla lista dei film noleggiati dal cliente con id clientID, e tale film, deve essere riaggiunto alla lista dei film disponibili in negozio (film_list). Successivamente, il metodo deve calcolare la penale che il cliente deve pagare utilizzando l'opposito metodo. Stampare la penale che il cliente deve pagare: "Cliente: {clientID}! La penale da pagare per il film {titolo_film} e' di {tot} euro!".

printMovies(): stampa la lista di tutti i film disponibili in negozio. Ogni film deve essere stampato in questo modo: "{titolo_film} - {genere_film} -"

printRentMovies(clientID): questo metodo deve stampare la lista dei film noleggiati dal cliente di cui viene specificato l'id.
'''


class Noleggio:

    _film_list:list[Film]
    _rented_film:dict[int, list[Film]]

    def __init__(self, film_list:list[Film]) -> None: 

        self._film_list = film_list 
        self._rented_film = {}
        self._movierented = []

    def isAvaible(self, film:Film) -> bool:
        
        if film in self._film_list:
            
            print(f"Il film scelto è disponibile: {film.getTitle()}!")
            return True 
        
        else:
            print(f"Il film scelto non è disponibile: {film.getTitle()}!")
            return False
            
    def rentAMovie(self, film:Film, clientID:int):

        if film in self._film_list:

            self._film_list.remove(film)
            self._movierented.append(film)
            
            self._rented_film[clientID] = self._movierented 

            print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
        
        else:
            print(f"Non è possibile nolegiare il film {film.getTitle()}!")

    def giveBack(self, film:Film, clientID:int, days:int):

        if film in self._rented_film[clientID]:

            self._rented_film[clientID].remove(film)
            self._film_list.append(film)

            print(f"Cliente: {clientID}! La penale da pagare per il film '{film.getTitle()}' è di {film.calcolaPenaleRitardo(days)} euro!")
        
        else:
            print(f"Non esiste il film '{film.getTitle()}' associato a questo ID!")

    def printMovies(self) -> None: 

        for films in self._film_list:
            print(f"{films.getTitle()} - {films.getGenere()}") 

    def printRentMovies(self, clientID:int) -> None:
        
        for id, movies in self._rented_film.items():

            if id == clientID:

                for movie in movies: 

                    print(f"{movie.getTitle()} - {movie.getGenere()}")

            else:
                print(f"Non esistono film associati a questo ID")
        


film1 = Azione("Ciao", 12)
film2 = Drama("Arrivederci", 21)
film3 = Commedia("Giorno", 69)
film4 = Commedia("Notte", 96)

print(film1.getPenale())
print(film2.getPenale())
print(film3.getPenale())

noleggio1 = Noleggio([film1,film2,film3])

# print(film2.getTitle())
# print(film2.calcolaPenaleRitardo(10))
# print(film2.getID())
# print(film2.getGenere())

# print(noleggio1.isAvaible(film4))
# noleggio1.isAvaible(film3)
# noleggio1.printMovies()

# noleggio1.rentAMovie(film1, 121212)

# print(" ")
# noleggio1.isAvaible(film1)
# noleggio1.printRentMovies(121212)

# noleggio1.rentAMovie(film2,121212)
# noleggio1.printRentMovies(121212)

# noleggio1.giveBack(film2, 121212, 5)
# print("")
# noleggio1.printRentMovies(121212)

noleggio1.rentAMovie(film1, 10)
noleggio1.rentAMovie(film2, 10)
noleggio1.printRentMovies(10)