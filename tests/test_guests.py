import unittest
from src.guests import Guests

class TestGuests(unittest.TestCase):

    def setUp(self):

        self.guest_1 = Guests("John", 50)
        self.guest_2 = Guests("Sam", 70)
        self.guest_3 = Guests("Julie", 20)
        self.guest_4 = Guests("Phoebe", 30)
        self.guest_5 = Guests("Harry", 40)
        self.guest_6 = Guests("Zoe", 5)
    

    def test_guest_has_name(self):
        self.assertEqual("John", self.guest_1.name)
    
    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest_1.wallet)