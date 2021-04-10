import unittest
from src.rooms import Rooms
from src.guests import Guests
from src.songs import Songs

class TestRooms(unittest.TestCase):

    def setUp(self):

        self.rooms_1 = Rooms("Gold")
        self.du_hast = Songs("Du Hast", "Rammstein")
        self.john = Guests("John")

    
    def test_room_has_name(self):
        self.assertEqual("Gold", self.rooms_1.name)
    
    def test_song_queue_is_0(self):
        self.assertEqual(0, len(self.rooms_1.song_queue))
    
    def test_add_song_to_song_queue(self):
        self.rooms_1.add_song_to_song_queue(self.du_hast)
        self.assertEqual(1, len(self.rooms_1.song_queue))
    
    def test_occupants_is_0(self):
        self.assertEqual(0, len(self.rooms_1.occupants))
    
    def test_add_occupant_to_room(self):
        self.rooms_1.add_occupant_to_room(self.john)
        self.assertEqual(1, len(self.rooms_1.occupants))
    


