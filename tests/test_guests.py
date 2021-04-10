import unittest
from src.guests import Guests

class TestGuests(unittest.TestCase):

    def setUp(self):

        self.guest_1 = Guests("John")
    

    def test_guest_has_name(self):
        self.assertEqual("John", self.guest_1.name)