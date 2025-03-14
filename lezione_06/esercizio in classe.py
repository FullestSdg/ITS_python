class Person:
   
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

print(bob.age)

if alice.age > bob.age:
    print(alice.name)

else:
    print(bob.name)

giovanni = Person("Giovanni M", 55)
francesco = Person("Francesco T.", 49)
sergio = Person("Sergio D.", 21)

people:list[Person] = [alice, bob, giovanni, francesco, sergio]
print(people)

min_name = alice.name
min_age = alice.age

for person in people:

    if person.age < min_age:

        min_age = person.age
        min_name = person.name

print(f"La persona con l'età più piccola è: {min_name}")



class Student:
    def __init__(self, name:str, studyProgram:str, age:int, gender:str):
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender
    
    def printInfo(self):
        print(f"{self.name}: {self.studyProgram}: {self.age} anni: {self.gender}")
    

sergio = Student("Sergio D", "CyberSecurity", 21, "Maschio")
domenico = Student("Domenico C.", "CyberSecurity", 19, "Maschio")
nessuno = Student("Nessuno N.", "Nessun corso", 0, "Sconosciuto")

sergio.printInfo()
domenico.printInfo()
nessuno.printInfo()