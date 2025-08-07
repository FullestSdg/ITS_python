'''
PARTE 1
In questo progetto, dovrai scrivere il codice per un sistema di gestione e creazione dei corsi ITS.
Il sistema gestisce aule ed edifici (Parte 1), persone -studenti e docenti- in gruppi di studio (parte 2), e corsi (parte 3).
 
### Classe Room:
La classe Room rappresenta un'aula. Ogni aula ha un ID (id), un piano (floor), un numero di posti (seats) e un'area (area). L'area è calcolata come il doppio dei posti.
- Metodi:
    - get_id(): Restituisce l'ID dell'aula.
    - get_floor(): Restituisce il piano dell'aula.
    - get_seats(): Restituisce il numero di posti dell'aula.
    - get_area(): Restituisce l'area dell'aula.

### Classe Building:
La classe Building rappresenta un edificio. Ogni edificio ha un nome (name), un indirizzo (address), un intervallo di piani (floors), e una lista di aule (rooms).
- Metodi:
    - get_floors(): Restituisce l'intervallo di piani dell'edificio.
    - get_rooms(): Restituisce la lista delle aule nell'edificio.
    - add_room(room): Aggiunge un'aula all'edificio, solo se il piano dell'aula è compreso nell'intervallo di piani dell'edificio.
    - area(): Restituisce l'area totale dell'edificio sommando le aree di tutte le aule.
 
PARTE 2
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
 
PARTE 3
### Classe Course:
La classe Course rappresenta un corso accademico. Ogni corso ha un nome (name) e una lista di gruppi (groups).
- Metodi:
    - register(student): Registra uno studente nel primo gruppo disponibile che non ha ancora raggiunto il limite di studenti.
    - get_groups(): Restituisce la lista dei gruppi nel corso.
    - add_group(group): Aggiunge un gruppo al corso.

'''
import math

class Room:

    def __init__(self, id:str, floor:str, seats:int) -> None:
         
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

    def get_area(self) -> int:
        return self.area

class Building:
    
    def __init__(self, name:str, address:str, floors:int, rooms:list[Room]) -> None:

        self.name = name 
        self.address = address 
        self.floors = floors 
        self.rooms = rooms 

    def get_floors(self) -> int: 
        return self.floors  

    def get_rooms(self) -> list[Room]:
        return self.rooms 

    def add_rooms(self, room:Room) -> None:

        if room.get_floor() <= self.floors:
            self.rooms.append(room)
        
        else:
            print("Impossibile aggiungere l'aula, non è compresa nell'intervallo")

    def area(self) -> int:

        area = 0

        for rooms in self.rooms:
            area += rooms.get_area()

        return area 

class Person:

    def __init__(self, cf:str, name:str, surname:str, age:int) -> None:
        
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age
    
    def setCF(self, cf:str) -> None:
        self.cf = cf
    
    def setName(self, name:str) -> None:
        self.name = name 
    
    def setSurname(self, surname:str) -> None:
        self.surname = surname

    def setAge(self, age:int) -> None:
        self.age = age

    def getCF(self) -> str:
        return self.cf 
    
    def getName(self) -> str:
        return self.name
    
    def getSurname(self) -> str:
        return self.surname

    def getAge(self) -> int:
        return self.age

class Student(Person):

    def __init__(self, cf:str, name:str, surname:str, age:int):
        super().__init__(cf, name, surname, age)
    
    def set_group(self, group) -> None:
        self.group = group

class Lecturer(Person):

    def __init__(self, cf:str, name:str, surname:str, age:int):
        super().__init__(cf, name, surname, age)

   
class Group:

    def __init__(self, name:str, limit:int, students:list[Student], lecturers:list[Lecturer] ) -> None:

        self.name = name 
        self.limit = limit 
        self.students = students 
        self.lecturers = lecturers

    def get_name(self) -> str:
        return self.name 
    
    def get_limit(self) -> int:
        return self.limit 
    
    def get_students(self) -> list[Student]:
        return self.students 
    
    def get_limit_lecturers(self) -> int:

        numero_studenti = len(self.students)
        limite_lecturers = 0

        if numero_studenti < 10:
            limite_lecturers += 1

        else:
            limite_lecturers += math.ceil(numero_studenti / 10)  
        
        return limite_lecturers
    
    def add_student(self, student:Student) -> None | str:

        if len(self.students) < self.limit:
            self.students.append(student)
        
        else:
            return f"Limite raggiunto impossibile aggiungere altri studenti"
    
    def add_lecturer(self, lecturer:Lecturer) -> None | str:

        if len(self.lecturers) < self.get_limit_lecturers():
            self.lecturers.append(lecturer)
            
        else:
            return f"Limite raggiunto impossibile aggiungere altri docenti"


class Course:

    def __init__(self, name:str, groups:list[Group]) -> None:

        self.name = name 
        self.groups = groups 

    def register(self, student:Student) -> None:

        for corsi in self.groups:

            if corsi.get_limit() == len(corsi.get_students()):
                continue 

            else:
                corsi.add_student(student)
    
    def get_groups(self) -> list[Group]:
        return self.groups 
    
    def add_group(self, group:Group) -> None:
        self.groups.append(group)