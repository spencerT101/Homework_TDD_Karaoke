import unittest
from src.rooms import Rooms
from src.guests import Guests
from src.songs import Songs

class TestRooms(unittest.TestCase):

    def setUp(self):

        self.rooms_1 = Rooms("Gold")
    
    def test_room_has_name(self):
        self.assertEqual("Gold", self.rooms_1.name)
    
    def test_song_queue_is_0(self):
        self.assertEqual(0, self.rooms_1.song_queue_is_0())
    
    def test_occupants_is_0(self):
        self.assertEqual(0, self.rooms_1.occupants_is_0())
    


