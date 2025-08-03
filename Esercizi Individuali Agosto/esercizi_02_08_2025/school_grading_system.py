'''
1. School Grading System:

Create a function that takes a student's name and their scores in different subjects as input.
The function calculates the average score and prints the student's name, average, and a message indicating whether the student passed the exam (average >= 60) or failed.
Create a for loop to iterate over a list of students and scores, calling the function for each student.
'''
from random import * 

def SchoolGradingSystem(scores:dict[str,dict[str,list[int]]]) -> str:

    somma = 0
    media = 0
    esito_esame = None

    for nome, values in scores.items():

        for materia, voti in values.items():

            for v in voti:

                somma += v
                media = somma / len(voti)

    if media >= 60:
        esito_esame = "Passato"
    else:
        esito_esame = "Non Passato"

    return f"Studente: {nome}\nMateria: {materia}\nMedia: {media:.2f}\nStato Esame: {esito_esame}"


students:list[str] = ["Sergio De Guidi", "Daniel Ercoli", "Giuseppe Roberto", "Davide Battista"]
subjects:list[str] = ["Matematica", "Inglese", "Storia"]

for studente in students:

    for materia in subjects:

        voti = [randint(10, 100) for i in range(4)]

        scores = {studente: {materia: voti}}

        print(SchoolGradingSystem(scores))
        print("\n")

    

