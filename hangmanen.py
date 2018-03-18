"""
Modified hangman with multiple songs as entries. Originaly designed for
use on DTForums' roulette games.
"""

from generic_functions import *
from Entry import *
from EP import *


def loadSongs(LIST_NAME, entries_list):

    """Loads the list of names from a text file, one per line."""

    with open(LIST_NAME + ".txt", "r", encoding='utf-8') as file:

        for line in file:

            entry = Entry()

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





def saveBlankNames(entries_list):

    """
    Since both artist and song have to be 'blanked', making a separate
    function is easier than copypasting the same code for each.
    """

    for entry in entries_list:
        entry.blank_artist = createBlankName(entry.artist)
        entry.blank_song = createBlankName(entry.song)


def invalidLetter(entries_list, guess):

    """
    Only replaces the letter if it exists on the entry, 
    otherwise prepare for hangman.
    """

    hangman = True
    guess_lower = guess.lower()
    guess_upper = guess.upper()

    for entry in entries_list:

        # The letter has to be checked in both the artist and song names, 
        # in lower and uppercase.
        if guess_lower in entry.artist:
            entry.blank_artist = entry.replaceLetter(entry.artist, guess_lower,
                                                     entry.blank_artist)
            hangman = False

        if guess_lower in entry.song:
            entry.blank_song = entry.replaceLetter(entry.song, guess_lower,
                                                   entry.blank_song)
            hangman = False

        if guess_upper in entry.artist:
            entry.blank_artist = entry.replaceLetter(entry.artist, guess_upper,
                                                     entry.blank_artist)
            hangman = False

        if guess_upper in entry.song:
            entry.blank_song = entry.replaceLetter(entry.song, guess_upper,
                                                   entry.blank_song)
            hangman = False

    return hangman


def invalidWords(entries_list, guess):

    """
    This assumes you're writing the words exactly as they written in 
    the entries. No spellchecking, this is case-sensitive. Enter either 
    artist or song name (or part of either) here, but not both.
    """

    for entry in entries_list:

        index = entry.artist.find(guess)

        if index != -1:
            entry.blank_artist = entry.replaceWords(entry.blank_artist, 
                                                    guess, index)
            
            return False

        else:
            index = entry.song.find(guess)

            if index != -1:
                entry.blank_song = entry.replaceWords(entry.blank_song, 
                                                      guess, index)

                return False

    else:
        return True


def checkGuess(entries_list, guess, guessed_letters, guessed_words):
    
    """
    It is important to separate what kind of guess the player is
    giving and save the correct ones.
    """
    
    while guess in guessed_letters or guess in guessed_words:
        print("\nGuess is already existing. Try another one.")
        guess = input("New guess: ")
    
    else:
        if isLetter(guess):
            if invalidLetter(entries_list, guess):
                print("ohnoes, a hangman!")
    
            else:
                # make a for loop and call the replace method?
                guessed_letters.append(guess)
    
        else:
            if invalidWords(entries_list, guess):
                print(guess)
                print("hangman D:")
            
            else:
                guessed_words.append(guess)
    
        return (guessed_letters, guessed_words)


def loadGuessesFile(LIST_NAME, entries_list, guessed_letters, guessed_words):
    
    """LIST_NAME must not end in '.txt'."""
    
    try:
        with open(LIST_NAME + ' guesses.txt', 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                
                if "\ufeff" in line:
                    line = line.replace("\ufeff", "")
                
                guessed_entries = checkGuess(entries_list, line, 
                                             guessed_letters, guessed_words)
                
                guessed_letters = guessed_entries[0]
                guessed_words = guessed_entries[1]

    except FileNotFoundError:
        file = open(LIST_NAME + ' guesses.txt', 'w', encoding='utf-8')
        file.close()
    
    finally:
        return guessed_letters


def checkComplete(entries_list):

    """If all entries have been guessed, game is over."""

    for entry in entries_list:
        if (entry.artist != entry.blank_artist 
            or entry.song != entry.blank_song):
            
            if not entry.guessed_player:
                return False
    
    else:
        return True


def promptUser():

    """Main game options."""

    while True:
        print("\n\n",
              "1. Guess a word or a letter. \n",
              "2. A player has been guessed. \n",
              "3. Exit. \n")

        choice = input("Choose one: ")
        
        if choice != "1" and choice != "2" and choice != "3":
            print("Error, insert a valid number.")

        else:
            break

    return choice


def saveGuess(LIST_NAME, guess):

    """Puts them in a text file to be loaded later."""

    with open(LIST_NAME + ' guesses.txt', 'a', encoding='utf-8') as file:
        file.write(guess + '\n')


def saveGuessedPlayer(LIST_NAME, player):
    
    """Same as above, but separate from it."""
    
    with open(LIST_NAME + " guessed players.txt", 
              "a", encoding="utf-8") as file:
        
        file.write(player + '\n')


def loadGuessedPlayers(LIST_NAME, entries_list):
    
    """Reads from a file then modifies the entry objects if it exists."""
    
    try:
        with open(LIST_NAME + ' guessed players.txt', 
                  'r', encoding='utf-8') as file:
            
            for line in file:
                line = line.strip()
                guessedPlayer(entries_list, line)
                

    except FileNotFoundError:
        file = open(LIST_NAME + ' guessed players.txt', 'w', encoding='utf-8')
        file.close()       
    
    
def guessedPlayer(entries_list, player):
    
    """
       Looks for the the player and makes it printable once it's 
       been guessed.
    """
    
    for entry in entries_list:
        if entry.player == player:
            entry.guessed_player = True
    
    return entry.guessed_player


def printBlankList(entries_list):

    """
    Prints it using the folloowing format:
       
       Player: Artist - Song
    """

    for entry in entries_list:
        if entry.guessed_player:
            print(entry.player, end=": ")
        
        else:
            print("?:", end=" ")
        
        print(entry.blank_artist, "-", entry.blank_song)


def printGuessedLetters(guessed_letters):

    """Helps to keep track of what's been guessed."""

    print("\nGuessed letters: ", end="")

    for letter in guessed_letters:
        print(letter.upper(), end=" ")


def main():
    LIST_NAME = askForName()
    entries_list = []
    entries_list = loadSongs(LIST_NAME, entries_list)
    guessed_letters = []
    guessed_words = []

    saveBlankNames(entries_list)
    loadGuessesFile(LIST_NAME, entries_list, guessed_letters, guessed_words)
    loadGuessedPlayers(LIST_NAME, entries_list)
    
    printBlankList(entries_list)
    printGuessedLetters(guessed_letters)

    while not checkComplete(entries_list):
        choice = promptUser()
        
        if choice == "1":
            guess = askGuess()
            guessed_entries = checkGuess(entries_list, guess, 
                                         guessed_letters, guessed_words)
            guessed_letters = guessed_entries[0]
            guessed_words = guessed_entries[1]
            
            if guess in guessed_letters or guess in guessed_words:
                saveGuess(LIST_NAME, guess)
        
        elif choice == "2":
            player = input("Write the name of the guessed player: ")
            guessedPlayer(entries_list, player)
            saveGuessedPlayer(LIST_NAME, player)
        
        elif choice == "3":
            break
        

        printBlankList(entries_list)
        printGuessedLetters(guessed_letters)        


            



main()