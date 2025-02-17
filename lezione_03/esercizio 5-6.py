age:int = int(input("Inserire un'età valida: "))

if age == 0 and age < 2:
    print("It's a baby!")
elif age >= 2 and age < 4:
    print("It's a toddler!")
elif age >= 4 and age < 13:
    print("It's a kid")
elif age >= 13 and age < 20:
    print("It's a teenager!")
elif age >= 20 and age < 65:
    print("It's an adult!")
elif age >= 65:
    print("It's an elder!")
else:
    print("Età inserita non valida")