import unittest
from src.songs import Songs 


class TestSongs(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Du Hast", "Rammstein")
    


    def test_song_has_name(self):
        self.assertEqual("Du Hast", self.song_1.name)
    

    
    



