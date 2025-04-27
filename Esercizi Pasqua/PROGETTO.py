'''
In questo progetto, dovrai scrivere il codice per un sistema di gestione e creazione dei corsi ITS.
Il sistema gestisce aule ed edifici (Parte 1), persone -studenti e docenti- in gruppi di studio (parte 2), e corsi (parte 3).
 
### Classe Room:
La classe Room rappresenta un'aula. Ogni aula ha un ID (id), un piano (floor), un numero di posti (seats) e un'area (area).
L'area è calcolata come il doppio dei posti.
- Metodi:
    - get_id(): Restituisce l'ID dell'aula.
    - get_floor(): Restituisce il piano dell'aula.
    - get_seats(): Restituisce il numero di posti dell'aula.
    - get_area(): Restituisce l'area dell'aula.

### Classe Building:
La classe Building rappresenta un edificio.
Ogni edificio ha un nome (name), un indirizzo (address), un intervallo di piani (floors), e una lista di aule (rooms).
- Metodi:
    - get_floors(): Restituisce l'intervallo di piani dell'edificio.
    - get_rooms(): Restituisce la lista delle aule nell'edificio.
    - add_room(room): Aggiunge un'aula all'edificio, solo se il piano dell'aula è compreso nell'intervallo di piani dell'edificio.
    - area(): Restituisce l'area totale dell'edificio sommando le aree di tutte le aule.
'''

class Room:

    def __init__(self, id:int, floor:int, seats:int, area:int) -> None:

        self.id = id
        self.floor = floor
        self.seats = seats
        self.area = seats * 2

    def get_id(self) -> int:

        return self.id
    
    def get_floor(self) -> int:

        return self.floor
    
    def get_seats(self) -> int:
        
        return self.seats
    
    def get_area(self)-> int:

        return self.area
    
class Building:

    def __init__(self, name:str, address:str, floors:int, rooms:list[int]) -> None:

        self.name = name
        self.address = address
        self.floors = floors
        self.rooms = []

    def get_floors(self) -> int:

        return self.floors
    
    def get_rooms(self) -> list[int]:

        return self.rooms
    
    def add_room(self, room:int) -> None:
        # - add_room(room): Aggiunge un'aula all'edificio, solo se il piano dell'aula è compreso nell'intervallo di piani dell'edificio.
        if Room.get_floor(self.floor) in self.floors:
            self.rooms.append(room)
    
    def area(self) -> int:

        return sum(Room.get_area() for r in self.rooms)





        
