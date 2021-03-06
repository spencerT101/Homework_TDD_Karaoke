class Rooms:

    def __init__(self, name, seats, fee):
        self.name = name
        self.occupants = []
        self.song_queue = []
        self.seats = seats
        self.fee = fee
        

    

    def song_queue_is_0(self):
        return len(self.song_queue)
    
    def add_song_to_song_queue(self, song):
        return self.song_queue.append(song)
    
    def remove_song_from_song_queue(self, song):
        return self.song_queue.remove(song)
    
    def occupants_is_0(self):
        return len(self.occupants)
    
    def checkin_occupant_to_room(self, occupant):
        return self.occupants.append(occupant)

    def checkout_occupant_from_room(self, occupant):
        return self.occupants.remove(occupant)
    
    def room_has_space(self, seat_taken):
        if seat_taken <= self.seats:

            return "Seats Available!"
        
        return "Sold Out!"
    
    def customer_can_afford_entry_fee(self, money):
        if money >= self.fee:

            return True
        
        return False