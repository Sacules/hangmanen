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


def loadSongs(LIST_NAME, songs_list):
    
    """Loads the list of names from a text file, one per line."""
    
    with open(LIST_NAME + ".txt", "r", encoding='utf-8') as file:

        for line in file:
            
            artist_and_song = Song()

            # line = "Player: Artist - Song\n" 
            line = line.strip()

            # temp = ["Player", "Artist - Song"]
            temp = line.split(": ", maxsplit = 1)
            artist_and_song.player = temp[0]

            # temp2 = ["Artist", "Song"]
            temp2 = temp[1].split(" - ", maxsplit = 1)
            artist_and_song.artist = temp2[0]
            artist_and_song.song = temp2[1]

            songs_list.append(artist_and_song)
        
        return songs_list
            

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


def saveBlankNames(songs_list):
    
    """Since both artist and song have to be 'blanked', making a separate function
    is easier than copypasting the same code for each."""
    
    for artist_and_song in songs_list:
        artist_and_song.blank_artist = createBlankName(artist_and_song.artist)
        artist_and_song.blank_song = createBlankName(artist_and_song.song)


def validGuess(songs_list, guess):
    
    """Since performance doesn't matter, just cheking if the guess is valid is
    enough for this fuction."""
    
    for artist_and_song in songs_list:
        
        if guess in artist_and_song.artist:
            return True
        
        elif guess in artist_and_song.song:
            return True
        
        else:
            return False


def replaceGuess(songs_list, guess):
    
    """...in the blank names."""
    
    pass
    

def loadGuessesFile(self):
    try:
        with open(LIST_NAME + ' guesses', 'r', encoding='utf-8') as file:
            for line in file:

                line = line.strip()
                
                if len(line) == 1:
                    replaceGuess(songs_list, guess)
                    replaceGuess(songs_list, guess)

                else:
                    replaceGuess(songs_list, guess)
                

    except FileNotFoundError:
        file = open(LIST_NAME + ' guesses', 'w', encoding='utf-8')
        file.close()


def askGuess(self, wrong):
    guess = input("Enter a word or letter to guess: ")
    
    if len(guess) == 1:
        wrong += replaceGuess(songs_list, guess)
        wrong += replaceGuess(songs_list, guess)
    
    else:
        wrong += replaceGuess(songs_list, guess)

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
    songs_list = []
    songs_list = loadSongs(LIST_NAME, songs_list)
    guessed_letters = []

    # This could be saved into a file then read of being generated each time,
    # but since performance doesn't matter here, I'll leave it that way
    saveBlankNames(songs_list)
    
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