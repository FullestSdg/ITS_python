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

    def __init__(self, id:str, floor:int, seats:int) -> None:

        self.id = id
        self.floor = floor
        self.seats = seats
        self.area = seats * 2

    def get_id(self) -> str:

        return self.id
    
    def get_floor(self) -> int:

        return self.floor
    
    def get_seats(self) -> int:
        
        return self.seats
    
    def get_area(self)-> int:

        return self.area
    
class Building:

    def __init__(self, name:str, address:str, floors:int) -> None:

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
        if room.get_floor(self.floors) in self.floors:
            self.rooms.append(room)
    
    def area(self) -> int:

        return sum(room.get_area() for room in self.rooms)
    

'''
### Classi Person, Student e Lecturer:
La classe Person rappresenta una persona con un codice fiscale (cf), un nome (name), un cognome (surname), un'età (age).
Le classi Student e Lecturer ereditano da Person.
Uno studente è associato ad un gruppo di studio (group). Quindi, la classe Student ha il seguente metodo:
    - set_group(group): Associa un gruppo di studio allo studente
### Classe Group:
La classe Group rappresenta un gruppo di studio. Ogni gruppo ha un nome (name), un limite di studenti (limit), una lista di studenti (students) e una lista di docenti (lecturers).
- Metodi:
    - get_name(): Restituisce il nome del gruppo
    - get_limit(): Restituisce il limite di studenti nel gruppo
    - get_students(): Resituisce la lista di studenti nel gruppo
    - get_limit_lecturers(): Restituisce il limite di docenti nel gruppo. E' consentito 1 docente ogni 10 studenti. Il gruppo può avere almeno 1 docente, anche se ci sono meno di 10 studenti.
    - add_student(student): Aggiunge uno studente al gruppo, solo se il limite per gli studenti non è stato raggiunto.
    - add_lecturer(lecturer): Aggiunge un docente al gruppo, solo se il limite per i docenti non è stato raggiunto.
'''

class Person:

    def __init__(self, cf:str, name:str, surname:str, age:int) -> None:

        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age

class Student(Person):

    def set_group(self, group:int) -> None:

        self.group = group

class Lecturer(Person):
    pass
    






        
