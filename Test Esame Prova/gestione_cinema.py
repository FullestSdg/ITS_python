from __future__ import annotations

class Ticket:

    ticket_id:str 
    movie:str 
    seat:str 
    is_booked:bool 

    def __init__(self):
        pass 

    def book(self) -> None:
        
        if self.is_booked == False:
            self.is_booked = True 
        
        else:
            print(f"Il biglietto per '{self.movie}' posto '{self.seat}' è già prenotato.")

    def cancel(self) -> None: 

        if self.is_booked == True:
            self.is_booked = False 
        
        else:
            print(f"Il biglietto per '{self.movie}' posto '{self.seat}' non risulta prenotato.")

class Viewer:

    viewer_id:str 
    name:str 
    booked_tickets:list[Ticket]

    def __init__(self):
        pass 

    def book_ticket(self, ticket:Ticket) -> None:

        if ticket.is_booked == False:
            self.booked_tickets.append(ticket)

            ticket.book()

        else:
            print(f"Il biglietto per '{ticket.movie}' non è disponibile.")

    def cancel_ticket(self, ticket:Ticket) -> None: 

        if ticket in self.booked_tickets:
            self.booked_tickets.remove(ticket)

            ticket.cancel()
        
        else: 
            print(f"Il biglietto per '{ticket.movie}' non è stato prenotato da questo spettatore.")
    
class Cinema:

        tickets: dict[str, Ticket]
        viewers: dict[str, Viewer]

        def __init__(self):
            self.tickets = {}
            self.viewers = {}

        def add_ticket(self, ticket_id:str, movie:str, seat:str) -> None:
            if ticket_id in self.tickets:
                print(f"Il biglietto con ID '{ticket_id}' esiste già.")

            else:
                self.tickets[ticket_id] = Ticket(ticket_id = ticket_id, movie = movie, seat = seat)
        
        def register_viewer(self, viewer_id:str, name:str) -> None: 

            if viewer_id in self.viewers:
                print(f"Lo spettatore con ID '{viewer_id}' è già registrato.")
            
            else:
                self.viewers[viewer_id] = Viewer(viewer_id = viewer_id, name = name)
        
        def book_ticket(self, viewer_id:str, ticket_id:str) -> None:

            if viewer_id in self.viewers and ticket_id in self.tickets:
                
                self.viewers[viewer_id].book_ticket(self.tickets[ticket_id]) 

            else: 
                print("Spettatore o biglietto non trovato.")

        def cancel_ticket(self, viewer_id:str, ticket_id:str) -> None:

            if viewer_id in self.viewers and ticket_id in self.tickets:

                self.viewers[viewer_id].cancel_ticket(self.tickets[ticket_id])
            
            else:
                print("Spettatore o biglietto non trovato.")
        
        def list_available_tickets(self) -> list[str]:
            
            available = []

            for ticket_id, ticket in self.tickets.items():

                if ticket_id == False:
                    available.append(ticket_id)

            return available

        def list_viewer_bookings(self, viewer_id:str) -> list[str] | str:

            if viewer_id not in self.viewers:
                return "Errore: spettatore non trovato."
            
            viewer = self.viewers[viewer_id]
            booked = []

            for ticket in viewer.booked_tickets:
                booked.append(ticket.ticket_id)

            return booked


