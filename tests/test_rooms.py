import unittest
from src.rooms import Rooms
from src.guests import Guests
from src.songs import Songs

class TestRooms(unittest.TestCase):

    def setUp(self):

        self.rooms_1 = Rooms("Gold", 5)
        self.rooms_2 = Rooms("Green", 4)
        self.du_hast = Songs("Du Hast", "Rammstein")
        self.john = Guests("John")
        self.sam = Guests("Sam")
        self.julie = Guests("Julie")
        self.phoebe = Guests("Phoebe")
        self.harry = Guests("Harry")
        self.zoe = Guests("Zoe")
    
    def test_room_has_name(self):
        self.assertEqual("Gold", self.rooms_1.name)
    
    def test_song_queue_is_0(self):
        self.assertEqual(0, len(self.rooms_1.song_queue))
    
    def test_add_song_to_song_queue(self):
        self.rooms_1.add_song_to_song_queue(self.du_hast)
        self.assertEqual(1, len(self.rooms_1.song_queue))
    
    def test_remove_song_from_song_queue(self):
        self.rooms_1.add_song_to_song_queue(self.du_hast)
        self.rooms_1.remove_song_from_song_queue(self.du_hast)
        self.assertEqual(0, len(self.rooms_1.song_queue))

    def test_occupants_is_0(self):
        self.assertEqual(0, len(self.rooms_1.occupants))
    
    def test_checkin_occupant_to_room(self):
        self.rooms_1.checkin_occupant_to_room(self.john)
        self.assertEqual(1, len(self.rooms_1.occupants))
    
    def test_checkout_occupant_from_room(self):
        self.rooms_1.checkin_occupant_to_room(self.john)
        self.rooms_1.checkout_occupant_from_room(self.john)
        self.assertEqual(0, len(self.rooms_1.occupants))
    
    def test_room_has_seats(self):
        self.assertEqual(5, self.rooms_1.seats)
    
    def test_room_has_space(self):
        self.rooms_1.checkin_occupant_to_room(self.john)
        seat_taken = len(self.rooms_1.occupants)
        self.assertEqual("Seats Available!", self.rooms_1.room_has_space(seat_taken))
    
    def test_room_has_no_space(self):
        self.rooms_1.checkin_occupant_to_room(self.john)
        self.rooms_1.checkin_occupant_to_room(self.sam)
        self.rooms_1.checkin_occupant_to_room(self.julie)
        self.rooms_1.checkin_occupant_to_room(self.phoebe)
        self.rooms_1.checkin_occupant_to_room(self.harry)
        self.rooms_1.checkin_occupant_to_room(self.zoe)
        seat_taken = len(self.rooms_1.occupants)
        self.assertEqual("Sold Out!", self.rooms_1.room_has_space(seat_taken))
    
    def test_move_occupant_to_another_room(self):
        self.rooms_1.checkin_occupant_to_room(self.sam)
        self.rooms_1.checkout_occupant_from_room(self.sam)
        self.rooms_2.checkin_occupant_to_room(self.sam)
        self.assertEqual(0, self.rooms_1.song_queue)
        self.assertEqual(1, self.rooms_2.song_queue)
    


