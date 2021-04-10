import unittest
from src.songs import Songs 


class TestSongs(unittest.TestCase):

    def setUp(self):
        self.song_1 = Songs("Du Hast", "Rammstein")
    


    def test_song_has_name(self):
        self.assertEqual("Du Hast", self.song_1.song_name)
    
    def test_song_has_artist(self):
        self.assertEqual("Rammstein", self.song_1.artist)
    

    
    



