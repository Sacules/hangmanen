from generic_functions import *
from Entry import *

class EP():
    
    """Simple container for several entries."""
    
    def __init__(self):
        
        self.entry_list_unguessed = []
        self.entry_list_guessed = []

        self.player_name = ""
        self.guessed_player = False
        
        self.EP_name = ""
        self.blank_EP_name = ""
    
    def loadEntry(self, entry):
        self.entry_list_unguessed.append(entry)
    
    def getPlayer(self, player_name):
        self.player_name = player_name
    
    def getEPName(self, EP_name):
        self.EP_name = EP_name
        
    def makeEPNameBlank(self, EP_name):
        self.blank_EP_name = createBlankName(EP_name)
    
    def guessedEntry(self, entry):
        self.entry_list_guessed.append(entry)
        self.entry_list_unguessed.remove(entry)

    def printGuessedEP(self):
        # Title
        if self.guessed_player:
            print(self.player_name. end=' ')

        else:
            print("?", end=': ')
        
        print(self.blank_EP_name)

        # Guessed entries
        for entry in self.entry_list_guessed:
            if entry.guessed_player:
                print(entry.blank_artist, "-", entry.blank_song)

    def printUnguessedEntries(self):
        for entry in self.entry_list_unguessed:
            entry.printEntry()