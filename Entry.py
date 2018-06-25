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

        else:
            print("Invalid guess!")

    def replaceEntryWord(self, word):
        if word in self.name:
            self.blank_name = replaceWord(self.name, self.blank_name, word)

        else:
            print("Invalid guess!")

    def printEntry(self):
        pass