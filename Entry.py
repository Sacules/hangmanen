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

    def replaceLetter(self, name, letter, replacing_name):

        """
        When a guessed letter is valid, all instances of it have
        to be replaced.
        """

        index_list = findIndexes(name, letter)

        # Since strings are immutable, we need to transform it into a list
        replacing_name = list(replacing_name)

        if index_list != []:
            for index in index_list:
                replacing_name[index] = letter

        # We put it as a string back again
        return "".join(replacing_name)

    def replaceWords(self, replacing_name, guess, index):
    
        """
        Assume this won't go out of index range. Please.
        """
    
        replacing_name = list(replacing_name)
        guess = list(guess)
    
        for character in guess:
            replacing_name[index] = character
            index += 1
        
        return "".join(replacing_name)
    
    def printEntry(self):
        if self.guessed_player:
            print(self.player, end=": ")
        
        else:
            print("?:", end=" ")
        
        print(self.blank_artist, "-", self.blank_song)