from film import Film


class Noleggio:

    _film_list:list[Film]
    _rented_film:dict[int, list[Film]]

    def __init__(self, film_list:list[Film]) -> None: 

        self._film_list = film_list 
        self._rented_film = {}

    def isAvaible(self, film:Film) -> bool:
        pass 

