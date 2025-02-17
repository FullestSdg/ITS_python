current_users:list = ["Franco", "Fabrizio", "Giancarlo", "Mario", "Luigi"]
new_users:list = ["Franco", "Carlo", "Giggi", "Christian", "Mario"]

for i in new_users:
    if i in current_users:
        print("The username", i , "is already used! Please use another username.")
    else:
        print("This username is available!")

current_users:list = ["Franco", "Fabrizio", "Giancarlo", "Mario", "Luigi"]

for i in new_users:
    i.upper()
    print(current_users)