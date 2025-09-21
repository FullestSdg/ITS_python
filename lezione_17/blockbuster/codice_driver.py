from film import *
from movie_genre import *
from noleggio import *

# ----- Codice Driver -----

# Creazione lista di 10 film
film_list = [
    Azione("Die Hard", 1),
    Azione("Mad Max", 2),
    Azione("John Wick", 3),
    Azione("Gladiator", 4),
    Azione("Terminator", 5),
    Commedia("Una Notte da Leoni", 6),
    Commedia("Scemo e più Scemo", 7),
    Commedia("Il Grande Lebowski", 8),
    Commedia("Zoolander", 9),
    Drama("Il Miglio Verde", 10)
]

# Creazione oggetto Noleggio
noleggio = Noleggio(film_list)

print("Quale film vuoi noleggiare?")

# Simulazione noleggi
# 1) Primo cliente noleggia un film
cliente1 = 101
film1 = film_list[0]   # Die Hard
noleggio.rentAMovie(film1, cliente1)

# 2) Primo cliente noleggia un secondo film
film2 = film_list[1]   # Mad Max
noleggio.rentAMovie(film2, cliente1)

# 3) Secondo cliente prova a noleggiare lo stesso film (Mad Max)
cliente2 = 202
noleggio.rentAMovie(film2, cliente2)  # Deve dare messaggio che non è disponibile

# 4) Secondo cliente noleggia un terzo film
film3 = film_list[2]   # John Wick
noleggio.rentAMovie(film3, cliente2)

# 5) Primo cliente restituisce il secondo film (Mad Max) con 3 giorni di ritardo
noleggio.giveBack(film2, cliente1, 3)

# 6) Stampare lista film disponibili in negozio
print("\nFilm disponibili in negozio:")
noleggio.printMovies()