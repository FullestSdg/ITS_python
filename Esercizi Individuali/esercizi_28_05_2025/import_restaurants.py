'''
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.
'''

from restaurant import Restaurant

restaurant:Restaurant = ("Ciao mamma", "italiana")

print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())

channel_club = Restaurant('the channel club', 'steak and seafood')  # Crea un'istanza della classe Restaurant con nome e tipo di cucina
channel_club.describe_restaurant()  # Visualizza una descrizione del ristorante
channel_club.open_restaurant()  # Mostra un messaggio che indica che il ristorante è aperto

#da chiedre prof