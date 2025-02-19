current_users:list = ["Franco", "Fabrizio", "Giancarlo", "Mario", "Luigi"]
new_users:list = ["Franco", "Carlo", "Giggi", "Christian", "Mario"]

for i in new_users:
    if i in current_users:
        print("The username", i , "is already used! Please use another username.")
    else:
        print("This username is available!")

current_users_upper = []

for i in current_users:
    current_users_upper.append(i.upper())
print(current_users_upper)
