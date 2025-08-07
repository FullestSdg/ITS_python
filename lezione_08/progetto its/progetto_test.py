from progetto import *

def test_room_and_building():
    print("=== TEST ROOM & BUILDING ===")
    
    # Creo aule
    room1 = Room("A101", 1, 20)
    room2 = Room("A102", 2, 30)
    room3 = Room("A103", 5, 25)  # Piano non valido (fuori range)

    # Creo edificio con 3 piani
    building = Building("ITS Tech", "Via Roma 10", 3, [])

    # Aggiungo le aule
    building.add_rooms(room1)  # ok
    building.add_rooms(room2)  # ok
    building.add_rooms(room3)  # errore previsto

    print("Aule aggiunte:", [r.get_id() for r in building.get_rooms()])
    print("Area totale edificio:", building.area(), "mq\n")


def test_students_and_group():
    print("=== TEST STUDENTI & GRUPPO ===")

    # Creo studenti
    studenti = [Student(f"CF{i}", f"Nome{i}", f"Cognome{i}", 20+i) for i in range(12)]

    # Creo docenti
    docente1 = Lecturer("L001", "Prof", "Rossi", 45)
    docente2 = Lecturer("L002", "Prof", "Bianchi", 50)

    # Creo gruppo con limite 10 studenti
    gruppo = Group("Python Dev", limit=10, students=[], lecturers=[])

    # Aggiungo 12 studenti (gli ultimi 2 devono fallire)
    for stud in studenti:
        result = gruppo.add_student(stud)
        if result:
            print("ERRORE:", result)
        else:
            stud.set_group(gruppo)

    print("Studenti nel gruppo:", len(gruppo.get_students()), "/", gruppo.get_limit())

    # Aggiunta docenti (12 studenti → limite docenti = 2)
    print("Limite docenti nel gruppo:", gruppo.get_limit_lecturers())

    res1 = gruppo.add_lecturer(docente1)
    res2 = gruppo.add_lecturer(docente2)
    res3 = gruppo.add_lecturer(Lecturer("L003", "Prof", "Verdi", 55))  # Deve fallire

    if res3:
        print("ERRORE:", res3)

    print("Docenti nel gruppo:", len(gruppo.lecturers), "\n")


def test_course_registration():
    print("=== TEST CORSO & ISCRIZIONI ===")

    # Crea due gruppi da 5 studenti ciascuno
    group1 = Group("Gruppo A", limit=5, students=[], lecturers=[])
    group2 = Group("Gruppo B", limit=5, students=[], lecturers=[])

    # Crea corso e aggiungi gruppi
    corso = Course("Data Science", groups=[])
    corso.add_group(group1)
    corso.add_group(group2)

    # Registra 8 studenti
    for i in range(8):
        student = Student(f"CS{i}", f"Stud{i}", "Test", 22)
        corso.register(student)

    # Verifica distribuzione
    for group in corso.get_groups():
        print(f"{group.get_name()}: {len(group.get_students())} studenti")

    # Prova a registrare altri 3 studenti → gli ultimi 2 devono fallire
    print("\n-- Test overflow studenti --")
    for i in range(8, 11):
        student = Student(f"CS{i}", f"Stud{i}", "Test", 22)
        corso.register(student)

    for group in corso.get_groups():
        print(f"{group.get_name()}: {len(group.get_students())} studenti (limite: {group.get_limit()})")

    print()


def run_all_tests():
    test_room_and_building()
    test_students_and_group()
    test_course_registration()


if __name__ == "__main__":
    run_all_tests()