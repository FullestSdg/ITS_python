'''
Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
'''

class Restaurant:

    def __init__(self, restaurant_name:str, cuisine_type:str) -> None:

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self) -> str:

        return f"Questo ristorante chiamato '{self.restaurant_name}' ha questo tipo di cucina: {self.cuisine_type}"
    
    def open_restaurant(self) -> str:

        return f"{self.restaurant_name} è aperto!"
    
restaurant:Restaurant = Restaurant("Da pippo er bibbo", "italiana")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())
