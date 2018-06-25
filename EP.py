from text_functions import *

class EP():

    def __init__(self, name, player):

        """Basic info each EP holds."""

        self.name = name
        self.blank_name = createBlankName(self.name)

        self.player = player
        self.guessed_player = False

        self.entries = []

    def addEntry(self, entry):
        self.entries.append(entry)

    def replaceEPNameLetter(self, letter):
        if letter in self.name:
            self.blank_name = replaceLetter(self.name, self.blank_name, letter)

        else:
            print("Invalid guess!")

    def replaceEPNameWords(self, word):
        if word in self.name:
            self.blank_name = replaceWord(self.name, self.blank_name, word)

        else:
            print("Invalid guess!")

    def printEP(self):
        pass

    def replaceEPEntryLetter(self, letter):
        for entry in self.entries:
            entry.replaceEntryLetter(letter)

    def replaceEPEntryWord(self, word):
        for entry in self.entries:
            entry.replaceEntryWord(word)
