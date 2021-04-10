class Rooms:

    def __init__(self, name):
        self.name = name
        self.occupants = []
        self.song_queue = []

    

    def song_queue_is_0(self):
        return len(self.song_queue)
    
    def add_song_to_song_queue(self, song):
        return self.song_queue.append(song)
    
    def occupants_is_0(self):
        return len(self.occupants)
    
    def add_occupant_to_room(self, occupant):
        return self.occupants.append(occupant)