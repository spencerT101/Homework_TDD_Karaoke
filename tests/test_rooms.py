import unittest
from src.rooms import Rooms
from src.guests import Guests
from src.songs import Songs
from tests.test_songs import TestSongs

class TestRooms(unittest.TestCase):

    def setUp(self):

        self.rooms_1 = Rooms("Gold", 5, 7)
        self.rooms_2 = Rooms("Green", 4, 8)
        self.du_hast = Songs("Du Hast", "Rammstein")
        self.john = Guests("John", 50)
        self.sam = Guests("Sam", 70)
        self.julie = Guests("Julie", 20)
        self.phoebe = Guests("Phoebe", 30)
        self.harry = Guests("Harry", 40)
        self.zoe = Guests("Zoe", 5)
    
    def test_room_has_name(self):
        self.assertEqual("Gold", self.rooms_1.name)
    
    def test_song_queue_is_0(self):
        self.assertEqual(0, len(self.rooms_1.song_queue))
    
    # def test_add_song_to_song_queue(self):
    #     Songs.song_1.song_name
    #     self.rooms_1.add_song_to_queue(song_1.song_name)
    #     self.assertEqual(1, len(self.rooms_1.song_queue))
    
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
        self.assertEqual(0, len(self.rooms_1.occupants))
        self.assertEqual(1, len(self.rooms_2.occupants))
    
    def test_customer_can_afford_entry_fee(self):
        money = self.john.wallet
        self.assertEqual(True, self.rooms_1.customer_can_afford_entry_fee(money))
    
    def test_customer_cannot_afford_entry_fee(self):
        money = self.zoe.wallet
        self.assertEqual(False, self.rooms_2.customer_can_afford_entry_fee(money))

    


