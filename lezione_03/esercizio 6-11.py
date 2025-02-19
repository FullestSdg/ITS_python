information1: dict = {"country":"USA","population":"9kk","fact":"the city which never sleeps"}
information2: dict = {"country":"New Zeland","population":"400k","fact":"eastern largest city of the world"}
information3: dict = {"country":"Australia","population":"5kk","fact":"most important city but not the capital"}

cities: dict = {"New York": information1,"Wellington": information2,"Sydney": information3}

print("New York",cities["New York"])
print("Wellington",cities["Wellington"])
print("Sydney",cities["Sydney"])

for città, informazione in cities.items():
    print(f"{città} = ")
