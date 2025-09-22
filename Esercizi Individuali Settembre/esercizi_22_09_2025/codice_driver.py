# main.py
from libro import Libro
from studente import Studente
from biblioteca import Biblioteca

def main():
    # 1. Creiamo 5 libri
    libro1 = Libro("Il signore degli anelli", "J.R.R. Tolkien", 1954)
    libro2 = Libro("1984", "George Orwell", 1949)
    libro3 = Libro("Orgoglio e pregiudizio", "Jane Austen", 1813)
    libro4 = Libro("I promessi sposi", "Alessandro Manzoni", 1827)
    libro5 = Libro("Il piccolo principe", "Antoine de Saint-Exupéry", 1943)

    # 2. Creiamo la lista di libri e la Biblioteca
    lista_libri = [libro1, libro2, libro3, libro4, libro5]
    biblioteca = Biblioteca(lista_libri)

    # 3. Creiamo due studenti
    studente1 = Studente("Alice", "S001")
    studente2 = Studente("Marco", "S002")

    # 4. Il primo studente prende in prestito 2 libri
    biblioteca.borrowBook(libro1, studente1.getID())
    biblioteca.borrowBook(libro2, studente1.getID())

    # 5. Il secondo studente prova a prendere un libro già preso
    biblioteca.borrowBook(libro1, studente2.getID())

    # 6. Il primo studente restituisce un libro
    biblioteca.returnBook(libro1, studente1.getID())

    # 7. Il secondo studente ora prende quel libro
    biblioteca.borrowBook(libro1, studente2.getID())

    # 8. Stampa libri disponibili e libri presi in prestito
    print("\n📚 Libri disponibili in biblioteca:")
    biblioteca.printAvailableBooks()

    print(f"\n📖 Libri presi da {studente1.getName()} ({studente1.getID()}):")
    biblioteca.printBorrowedByStudents(studente1.getID())

    print(f"\n📖 Libri presi da {studente2.getName()} ({studente2.getID()}):")
    biblioteca.printBorrowedByStudents(studente2.getID())

if __name__ == "__main__":
    main()


