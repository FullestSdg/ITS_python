alien_color = input("Inserire un colore tra green, yellow, red: ")

if alien_color == "green":
    print("You earned 5 points!")
elif alien_color == "yellow":
    print("You earned 10 points!")
elif alien_color == "red":
    print("You earned 15 points!")
else: 
    print("Insert color non-valid")