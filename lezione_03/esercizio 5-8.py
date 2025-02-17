users:list = ["Marco", "Gino", "Admin", "Anna", "Roberto"]

for i in users:
    if i == "Admin":
        print("Hello Admin, would you like yo see a status report?")
    else:
        print("Hello,", i, "thank you for logging in")