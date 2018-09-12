import text_functions as txt


class Entry():
    def __init__(self, name, player):

        """Basic info each entry holds."""

        self.name = name
        self.blank_name = txt.createBlankName(self.name)

        self.player = player
        self.guessed_player = False

    def replaceLetter(self, letter):
        self.blank_name = txt.replaceLetter(self.name, self.blank_name, letter)

    def replaceEntryWord(self, word):
        self.blank_name = txt.replaceWord(self.name, self.blank_name, word)

    def printFormatted(self):
        if self.guessed_player:
            print(self.player + ":", self.blank_name)

        else:
            print("?:", self.blank_name)
