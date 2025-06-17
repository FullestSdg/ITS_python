'''
9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again. Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business. 

'''

class Restaurant:

    def __init__(self, restaurant_name:str, cuisine_type:str, number_served:int=0) -> None:

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self) -> str:

        return f"Questo ristorante chiamato '{self.restaurant_name}' ha questo tipo di cucina: {self.cuisine_type}"
    
    def open_restaurant(self) -> str:

        return f"{self.restaurant_name} è aperto!"
    
    def set_number_served(self, number_served:int) -> None:

        self.number_served = number_served

    def increment_number_served(self, additional_number_served:int) -> None:

        self.number_served += additional_number_served
    
restaurant:Restaurant = Restaurant("Francesco Totti", "italiana", 10)
print(restaurant.number_served)

restaurant2:Restaurant = Restaurant("Francesco Totti", "italiana")
print(restaurant2.number_served)

restaurant3:Restaurant = Restaurant("Francesco Totti", "italiana")
restaurant3.set_number_served(15)
restaurant3.increment_number_served(20)
print(restaurant3.number_served)
