from generic_functions import *

class Entry():
    
    def __init__(self):
        
        """Basic info each entry holds."""
        
        self.player = ""
        self.guessed_player = False
        
        self.artist = ""
        self.blank_artist = ""
        
        self.song = ""
        self.blank_song = ""

    def printEntry(self):
        if self.guessed_player:
            print(self.player, end=": ")
        
        else:
            print("?:", end=" ")
        
        print(self.blank_artist, "-", self.blank_song)
    
    def replaceBlankArtist(self, guess, index):
        self.blank_artist = replaceWords(self.blank_artist, guess, index)
    
    def replaceBlankSong(self, guess, index):
        self.blank_song = replaceWords(self.blank_song, guess, index)            