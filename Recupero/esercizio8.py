class Movie:

    def __init__(self, movie_id:str, title:str, director:str, is_rented:bool = False) -> None:

        self.movie_id = movie_id
        self.title = title
        self.director = director 
        self.is_rented = is_rented 
    
    def rent(self) -> None:

        if self.is_rented: #Sarebbe usuale a self.is_rented == True

            print("Errore: il film è già stato noleggiato!")

        else:

            self.is_rented = True

    def return_movie(self) -> None:

        if not self.is_rented:

            print("Errore: il film non è stato affittato a nessuno!")

        else:

            self.is_rented = False


class Customer:

    def __init__(self, customer_id:str, name:str) -> None:

        self.customer_id = customer_id 
        self.name = name 
        self.rented_movies:list[Movie] = []

    def rent_movie(self, movie:Movie) -> None:

        if movie.is_rented:

            print("Errore il film è già stato affittato a qualcuno")
        
        else:

            movie.rent()
            self.rented_movies.append(movie)
    
    def return_movie(self, movie:Movie) -> None:

        if movie in self.rented_movies:

            movie.return_movie()
            self.rented_movies.remove(movie)
        
        else:

            print("Errore: il cliente non ha noleggiato questo film!")


class VideoRentalStore:

    def __init__(self, movies:dict[str,Movie] = {}, customers:dict[str,Customer] = {}) -> None:

        self.movies = movies
        self.customers = customers 

    def add_movie(self, movie_id:str, title:str, director:str) -> None:

        if movie_id not in self.movies:

            movie:Movie = Movie(movie_id, title, director)

            # self.movies[movie_id] = movie

            tupla:tuple = (movie_id, movie)

            self.movies.update(tupla)
    
        else:

            print("Il film è già all'interno del catalogo")

    def register_customer(self, customer_id:str, name:str) -> None:

        if customer_id not in self.customers:

            customer:Customer = Customer(customer_id, name)

            self.customers[customer_id] = customer

            #tupla2:tuple = (customer_id, customer)

            #self.customers.updated(tupla2)

        else:

            print("Il cliente è già presente nell'anagrafica!")

    def rent_movie(self, customer_id:str, movie_id:str) -> None:

        if movie_id in self.movies and customer_id in self.customers:

            movie:Movie = self.movies[movie_id]

            self.customers[customer_id].rent_movie(movie)

        else:

            print("Cliente o Film non trovato!")

    def return_movie(self, customer_id:str, movie_id:str) -> None:

        if movie_id in self.movies and customer_id in self.customers:

            movie:Movie = self.movies[movie_id]

            self.customers[customer_id].return_movie(movie)

        else:

            print("Cliente o Film non trovato!")
    
    def get_rented_movies(self, customer_id:str) -> list[Movie]:

        if customer_id in self.customers:

            return self.customers[customer_id].rented_movies
        
        else:

            print("Il cliente non esiste!")

    def get_all_movies(self) -> list[Movie]:

        film_noleggiati:list[Movie] = []

        for customer_id, customer in self.customers.items():

            film_noleggiati += customer.rented_movies

        return film_noleggiati

