from text_functions import *

class Entry():
    def __init__(self, name, player):

        """Basic info each entry holds."""

        self.name = name
        self.blank_name = createBlankName(self.name)

        self.player = player
        self.guessed_player = False

    def replaceEntryLetter(self, letter):
        if letter in self.name:
            self.blank_name = replaceLetter(self.name, self.blank_name, letter)
            return True

        else:
            return False

    def replaceEntryWord(self, word):
        if word in self.name:
            self.blank_name = replaceWord(self.name, self.blank_name, word)
            return True

        else:
            return False

    def printEntry(self):
        if self.guessed_player:
            print(self.player + ":", self.blank_name)

        else:
            print("?:", self.blank_name)