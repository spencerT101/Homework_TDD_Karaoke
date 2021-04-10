import unittest
from src.guests import Guests

class TestGuests(unittest.TestCase):

    def setUp(self):

        self.guest_1 = Guests("John")
        self.guest_2 = Guests("Sam")
        self.guest_3 = Guests("Julie")
        self.guest_4 = Guests("Phoebe")
        self.guest_5 = Guests("Harry")
        self.guest_6 = Guests("Zoe")
    

    def test_guest_has_name(self):
        self.assertEqual("John", self.guest_1.name)