class Rooms:

    def __init__(self, name):
        self.name = name
        self.occupants = []
        self.song_queue = []

    

    def song_queue_is_0(self):
        return len(self.song_queue)
    
    
    
    def occupants_is_0(self):
        return len(self.occupants)