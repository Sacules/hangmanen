"""
Modified hangman with multiple songs as entries. Originaly designed for
use on DTForums' roulette games.
"""
from Song import *


def askForName():
        
    """A simple user prompt."""
        
    print("Name of the text file to load (without the extension): ", end="")
        
    LIST_NAME = input()
    
    return LIST_NAME


def loadSongs(LIST_NAME, entries_list):
    
    """Loads the list of names from a text file, one per line."""
    
    with open(LIST_NAME + ".txt", "r", encoding='utf-8') as file:

        for line in file:
            
            entry = Song()

            # line = "Player: Artist - Song\n" 
            line = line.strip()

            # temp = ["Player", "Artist - Song"]
            temp = line.split(": ", maxsplit = 1)
            entry.player = temp[0]

            # temp2 = ["Artist", "Song"]
            temp2 = temp[1].split(" - ", maxsplit = 1)
            entry.artist = temp2[0]
            entry.song = temp2[1]

            entries_list.append(entry)
        
        return entries_list
            

def createBlankName(name):
    
    """Based on the names loaded, creates the blanks for the player to
    guess. They're saved in a text file."""
    
    new_name = ""
    
    for letter in name:
        if letter == " ":
            new_name = new_name + " "
        
        elif letter == "-":
            new_name = new_name + "-"
        
        elif letter == "(":
            new_name = new_name + "("
        
        elif letter == ")":
            new_name = new_name + ")"
        
        elif letter == ",":
            new_name = new_name + ","
        
        elif letter == ":":
            new_name = new_name + ":"
            
        elif letter == "?":
            new_name = new_name + "?"
        
        elif letter == ".":
            new_name = new_name + "."
        
        elif letter == "'":
            new_name = new_name + "'"
        
        elif letter == "&":
            new_name = new_name + "&"
        
        else:
            new_name = new_name + "_"

    return new_name


def saveBlankNames(entries_list):
    
    """Since both artist and song have to be 'blanked', making a separate function
    is easier than copypasting the same code for each."""
    
    for entry in entries_list:
        entry.blank_artist = createBlankName(entry.artist)
        entry.blank_song = createBlankName(entry.song)


def isLetter(words):
    
    """This looks nicer and more understandable instead of just using the comparison."""
    
    return len(words) == 1


def findIndexes(word, letter):
    
    """Iterates over a word and returns a list with the positions in which
    a letter apears on it."""
    
    index = 0
    index_list = []
    
    for character in word:
        if character == letter:
            index_list.append(index)
        
        index += 1
    
    return index_list
    

def replaceLetters(name, letter, replacing_name):
    
    index_list = findIndexes(name, letter)
    
    # Since strings are immutable, we need to transform it into a list
    replacing_name = list(replacing_name)
    
    if index_list != []:
        for index in index_list:
            replacing_name[index] = letter
    
    # We put it as a string back again
    return "".join(replacing_name)


def invalidLetter(entries_list, guess):
    
    """Only replaces the letter if it exists on the entry, otherwise prepare for hangman."""
    
    hangman = True
    guess_lower = guess.lower()
    guess_upper = guess.upper()
    
    for entry in entries_list:
        
        # There will only be hangman if none of these is valid
        if guess_lower in entry.artist:
            entry.blank_artist = replaceLetters(entry.artist, guess_lower, entry.blank_artist)
            hangman = False

        if guess_lower in entry.song:
            entry.blank_song = replaceLetters(entry.song, guess_lower, entry.blank_song)
            hangman = False

        if guess_upper in entry.artist:
            entry.blank_artist = replaceLetters(entry.artist, guess_upper, entry.blank_artist)
            hangman = False

        if guess_upper in entry.song:
            entry.blank_song = replaceLetters(entry.song, guess_upper, entry.blank_song)
            hangman = False

    return hangman


def invalidWords(entries_list, guess):
    pass


def loadGuessesFile(self):
    try:
        with open(LIST_NAME + ' guesses', 'r', encoding='utf-8') as file:
            for line in file:

                line = line.strip()
                
                if len(line) == 1:
                    replaceGuess(entries_list, gues)
                    replaceGuess(entries_list, gues)

                else:
                    replaceGuess(entries_list, gues)
                

    except FileNotFoundError:
        file = open(LIST_NAME + ' guesses', 'w', encoding='utf-8')
        file.close()


def askGuess(self, wrong):
    guess = input("Enter a word or letter to guess: ")
    
    if len(guess) == 1:
        wrong += replaceGuess(entries_list, gues)
        wrong += replaceGuess(entries_list, gues)
    
    else:
        wrong += replaceGuess(entries_list, gues)

    # Saves correct guesses
    if wrong != 0:
        self.saveGuess(guess)


def checkComplete(self):
    
    """Checks if all the letters or words have been guessed."""
    
    for name in self.blank_names:
        
        for item in name:
            
            if "_" in item:
                return False
    
    return True


def askWordOrLetter(self):
    
    """Prompts the user to choose what to guess."""
    
    while True:
        print("\n",
              "1. Guess a word or a letter. \n",
              "2. Exit. \n")
        
        choice = input("Choose one: ")
        choice = int(choice)
        
        if choice != 1 and choice != 2:
            print("Error, insert a valid number.")

        else:
            break
    
    return choice


def saveGuess(self, guess):

    """Puts them in a text file to be loaded later."""

    with open(LIST_NAME + ' guesses', 'a', encoding='utf-8') as file:
        file.write(guess + '\n')




def printBlankList(self, printPlayers):
    
    """Kinda obvious isn't it?"""
    
    # A little something to help me print the player names
    i = 0
    
    for name in self.blank_names:

        item_pos = 0
        
        print("?:", end=" ")
        
        if printPlayers:
            new_name = ["".join(name[0]), "".join(name[1])]
        
            if new_name == self.names[i]:
                print(self.players[i], end=": ")
        
        for item in name:
            
            # Prints the word
            for letter in item:
                print(letter, end="")
            
            # After printing the artist, print a bar
            if item_pos == 0:
                print(" - ", end="")
                item_pos += 1
        
        # New line after each song
        print()
    
    # New line at the end
    print()


def printGuessedLetters(guessed_letters):
    
    """Won't even bother to explain this."""
    
    print("Guessed letters: ", end="")
    
    for letter in guessed_letters:
        print(letter.upper(), end=" ")
    
    print()
    

def main():
    # Important variables and lists
    LIST_NAME = askForName()
    entries_list = []
    entries_list = loadSongs(LIST_NAME, entries_list)
    guessed_letters = []

    # This could be saved into a file then read, instead of being generated each run,
    # but since performance doesn't matter here, I'll leave it that way
    saveBlankNames(entries_list)

    if invalidLetter(entries_list, "z"):
        print("ohnoes, a hangman!")
    
    else:
        print("no hangman fuck yeah. also you should save the guess here")
        
    for i in entries_list:
        print(i.blank_artist, "-", i.blank_song)
    
    #loadGuessesFile()
    #printBlankList(False)
    #printGuessedLetters()
    
    #while checkComplete() == False:
        #wrong = 0    
        #choice = askWordOrLetter()
        
        #if choice == 2:
            #break
        
        #else:
            #askGuess(wrong)
            #printBlankList(False)
            #printGuessedLetters()



main()