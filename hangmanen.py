"""
Modified hangman with multiple songs as entries. Originaly designed for
use on DTForums' roulette games.
"""
from Entry import *


def askForName():

    """A simple user prompt."""

    print("Name of the text file to load (without the extension): ", end="")

    LIST_NAME = input()

    return LIST_NAME


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


def replaceWords(replacing_name, guess, index):

    """Assume this won't go out of index range. Please."""

    replacing_name = list(replacing_name)
    guess = list(guess)

    for character in guess:
        replacing_name[index] = character
        index += 1
    
    return "".join(replacing_name)


def invalidWords(entries_list, guess):

    """This assumes you're writing the words exactly as they written in the entries.
       No spellchecking, this is case-sensitive. Enter either artist or song name
       (or part of either) here, but not both."""

    hangman = True

    for entry in entries_list:

        index = entry.artist.find(guess)

        if index != -1:
            entry.blank_artist = replaceWords(entry.blank_artist, guess, index)
            hangman = False
            break

        else:
            index = entry.song.find(guess)

            if index != -1:
                entry.blank_song = replaceWords(entry.blank_song, guess, index)
                hangman = False
                break

    return hangman


def checkGuess(entries_list, guess, guessed_letters, guessed_words):
    if isLetter(guess):
        if invalidLetter(entries_list, guess):
            print("ohnoes, a hangman!")

        else:
            guessed_letters.append(guess)

    else:
        if invalidWords(entries_list, guess):
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
                guessed_entries = checkGuess(entries_list, line, guessed_letters, guessed_words)
                guessed_letters = guessed_entries[0]
                guessed_words = guessed_entries[1]
                

    except FileNotFoundError:
        file = open(LIST_NAME + ' guesses.txt', 'w', encoding='utf-8')
        file.close()
    
    return guessed_letters


def askGuess():
    
    """Water is wet."""
    
    guess = input("Enter a word or letter to guess: ")
    
    return guess


def checkComplete(entries_list):

    """Checks if all the entried and players have been guessed."""

    for entry in entries_list:
        if entry.artist != entry.blank_artist or entry.song != entry.blank_song:
            if not entry.guessed_player:
                return False

    return True


def promptUser():

    """Gives the user some basic options."""

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
    
    with open(LIST_NAME + " guessed players.txt", "a", encoding="utf-8") as file:
        file.write(player + '\n')


def loadGuessedPlayers(LIST_NAME, entries_list):
    
    """Reads from a file then modifies the entry objects if it exists."""
    
    try:
        with open(LIST_NAME + ' guessed players.txt', 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                guessedPlayer(entries_list, line)
                

    except FileNotFoundError:
        file = open(LIST_NAME + ' guessed players.txt', 'w', encoding='utf-8')
        file.close()       
    
    
def guessedPlayer(entries_list, player):
    
    """Makes the player printable once it's been guessed."""
    
    for entry in entries_list:
        if entry.player == player:
            entry.guessed_player = True
    
    return entry.guessed_player


def printBlankList(entries_list):

    """Player: Artist - Song"""

    for entry in entries_list:
        if entry.guessed_player:
            print(entry.player, end=": ")
        
        else:
            print("?:", end=" ")
        
        print(entry.blank_artist, "-", entry.blank_song)


def printGuessedLetters(guessed_letters):

    """Mandatory docstring for consistent and aesthetic reasons."""

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
            guessed_entries = checkGuess(entries_list, guess, guessed_letters, guessed_words)
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