'''
9-15. Lottery Analysis: Extend the LotteryMachine class you created in Exercise 9-14.

1. Add a method called simulate_until_win(self, my_ticket) that:

Accepts a ticket (a list of 4 items).
Repeatedly draws random tickets using the draw_ticket() method.
Keeps count of how many attempts it takes until a randomly drawn ticket matches my_ticket.
Returns the number of attempts and the winning ticket.
2. Create a ticket called my_ticket with 4 numbers or letters from the pool.

3. Use the simulate_until_win() method to simulate how many draws it would take for your ticket to win.

4. Print a message showing:

Your ticket
The winning ticket
How many attempts it took to win
'''
from random import choice  # Import function to randomly select items

class LotteryMachine:
    """A class to simulate a simple lottery machine."""

    def __init__(self) -> None:
        """Initialize the machine with a pool of 10 numbers and 5 letters."""
        self.pool: list[str] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'a', 'b', 'c', 'd', 'e']  # Combined pool of numbers and letters
        self.winning_ticket: list[str] = []  # List to hold the winning ticket

    def draw_winning_ticket(self) -> list[str]:
        """Randomly select 4 unique items from the pool to create the winning ticket."""
        self.winning_ticket = []
        while len(self.winning_ticket) < 4:
            pulled: str = choice(self.pool)
            if pulled not in self.winning_ticket:
                self.winning_ticket.append(pulled)

        return self.winning_ticket

    def announce_winner(self) -> None:
        """Display a message with the winning ticket."""
        print("The winning ticket is:", self.winning_ticket)
        print("Any ticket matching these 4 items wins a prize!")


    def simulate_until_win(self, my_ticket: list[str]) -> tuple[int, list[str]]:
        """
        Simulate drawing tickets until one matches the given ticket.

        Args:
            my_ticket (list[str]): The user's ticket to match.

        Returns:
            tuple[int, list[str]]: Number of attempts and the winning ticket.
        """
        attempts = 0
        while True:
            new_ticket = self.draw_winning_ticket()
            attempts += 1
            if sorted(new_ticket) == sorted(my_ticket):
                return attempts, new_ticket


# Define a user ticket
my_ticket: list[str] = ['3', 'a', '7', 'd']

# Create the machine and simulate until a win
machine = LotteryMachine()
attempts, winning_ticket = machine.simulate_until_win(my_ticket)

# Print the result
print(f"Your ticket: {my_ticket}")
print(f"Winning ticket: {winning_ticket}")
print(f"It took {attempts} attempts to win.")