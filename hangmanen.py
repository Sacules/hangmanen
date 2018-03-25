"""
Modified hangman with multiple songs as entries. Originaly designed for
use on DTForums' roulette games.
"""

from random import shuffle

from generic_functions import *
from Entry import *
from EP import *

IS_EP_ROUND = False

def loadSongs(LIST_NAME, entries_list):

    """
    Loads the list of names from a text file, one per line.
    """

    with open(LIST_NAME + ".txt", "r", encoding='utf-8') as file:
        if IS_EP_ROUND:
            for line in file:
                # EPs begin with:
                # Player: Title
                title_line = line.split(": ", maxsplit=1)
                
                if len(title_line) == 2:
                    EP_entry = EP()
                    entries_list.append(EP_entry)
                    EP_entry.getPlayer(title_line[0])
                    EP_entry.getEPName(title_line[1].strip())                    

                # Parsing the EP
                if len(title_line) == 1 and line != "\n":
                    line = line.strip()
                    EP_line = line.split(" - ", maxsplit = 1)

                    track_entry = Entry()
                    
                    track_entry.artist = EP_line[0]
                    track_entry.song = EP_line[1]
                    track_entry.player = EP_entry.player_name
                    
                    EP_entry.loadEntry(track_entry)


        else:        
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

# I think this is kinda redundant, maybe move the functions as methods
def saveBlankNames(entries_list):

    """
    Since both artist and song have to be 'blanked', making a separate
    function is easier than copypasting the same code for each.
    """
    if IS_EP_ROUND:
        for EP_entry in entries_list:
            EP_entry.makeEPNameBlank()
            
            for song_entry in EP_entry.entry_list_unguessed:
                song_entry.blank_artist = createBlankName(song_entry.artist)
                song_entry.blank_song = createBlankName(song_entry.song)

    else:
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
    
    if IS_EP_ROUND:
        for EP_entry in entries_list:
            for song_entry in EP_entry.entry_list_unguessed:
                # The letter has to be checked in both the artist and song names, 
                # in lower and uppercase.
                if guess_lower in song_entry.artist:
                    song_entry.blank_artist = replaceLetter(song_entry.artist, guess_lower,
                                                               song_entry.blank_artist)
                    hangman = False
            
                if guess_lower in song_entry.song:
                    song_entry.blank_song = replaceLetter(song_entry.song, guess_lower,
                                                             song_entry.blank_song)
                    hangman = False
            
                if guess_upper in song_entry.artist:
                    song_entry.blank_artist = replaceLetter(song_entry.artist, guess_upper,
                                                               song_entry.blank_artist)
                    hangman = False
            
                if guess_upper in song_entry.song:
                    song_entry.blank_song = replaceLetter(song_entry.song, guess_upper,
                                                             song_entry.blank_song)
                    hangman = False
        
            if guess_lower in EP_entry.EP_name:
                EP_entry.blank_EP_name = replaceLetter(EP_entry.EP_name, guess_lower, 
                                                           EP_entry.blank_EP_name)            
            
            if guess_upper in EP_entry.EP_name:
                EP_entry.blank_EP_name = replaceLetter(EP_entry.EP_name, guess_upper, 
                                                       EP_entry.blank_EP_name)

    else:
        for entry in entries_list:
    
            # The letter has to be checked in both the artist and song names, 
            # in lower and uppercase.
            if guess_lower in entry.artist:
                entry.blank_artist = replaceLetter(entry.artist, guess_lower,
                                                         entry.blank_artist)
                hangman = False
    
            if guess_lower in entry.song:
                entry.blank_song = replaceLetter(entry.song, guess_lower,
                                                       entry.blank_song)
                hangman = False
    
            if guess_upper in entry.artist:
                entry.blank_artist = replaceLetter(entry.artist, guess_upper,
                                                         entry.blank_artist)
                hangman = False
    
            if guess_upper in entry.song:
                entry.blank_song = replaceLetter(entry.song, guess_upper,
                                                       entry.blank_song)
                hangman = False

    return hangman


def findWord(entry, guess):
    # Looks into the artist
    index = entry.artist.find(guess)

    if index != -1:
        return True

    # Looks into the song
    else:
        index = entry.song.find(guess)

        if index != -1:
            return True


def invalidWords(entries_list, guess):

    """
    This assumes you're writing the words exactly as they written in
    the entries. No spellchecking, this is case-sensitive. Enter either
    artist or song name (or part of either) here, but not both.
    """
    
    invalid = False
    
    if IS_EP_ROUND:
        for EP_entry in entries_list:
            for entry in EP_entry.entry_list_unguessed:
                invalid = invalid or findWord(entry, guess)

    else:
        for entry in entries_list:
            invalid = invalid or findWord(entry, guess)
    
    return not invalid


def fillCorrectWords(entries_list, guess):
    if IS_EP_ROUND:
        for EP_entry in entries_list:
            for song_entry in EP_entry.entry_list_unguessed:
                # Looks into the artist
                index = song_entry.artist.find(guess)
                if index != -1:
                    song_entry.replaceBlankArtist(guess, index)
            
                # Looks into the song
                index = song_entry.song.find(guess)
                if index != -1:
                    song_entry.replaceBlankSong(guess, index)                
    
    else:
        for entry in entries_list:
            # Looks into the artist
            index = entry.artist.find(guess)
            if index != -1:
                entry.replaceBlankArtist(guess, index)
    
            # Looks into the song
            index = entry.song.find(guess)
            if index != -1:
                entry.replaceBlankSong(guess, index)


def checkGuess(entries_list, guess, guessed_letters, guessed_words):

    """
    It is important to separate what kind of guess the player is
    giving and save the correct ones.
    """

    while guess in guessed_letters or guess in guessed_words:
        print("\nGuess is already existing. Try another one.")
        guess = input("New guess: ")

    if isLetter(guess) and not invalidLetter(entries_list, guess):
        guessed_letters.append(guess)

    elif not invalidWords(entries_list, guess):
        fillCorrectWords(entries_list, guess)
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

    all_guessed = False

    if IS_EP_ROUND:
        pass

    else:
        for entry in entries_list:
            if (entry.artist != entry.blank_artist 
                or entry.song != entry.blank_song):
                    all_guessed = all_guessed and entry.guessed_player
    
    return all_guessed


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
    
    if IS_EP_ROUND:
        for EP_entry in entries_list:
            for song_entry in EP_entry.entry_list_unguessed:
                if song_entry.player == player:
                    song_entry.guessed_player = True

    else:
        for entry in entries_list:
            if entry.player == player:
                entry.guessed_player = True

    return True


def printBlankList(entries_list, random_songs_list):

    """
    Prints using the following format:

       Player: Artist - Song
    """
    if IS_EP_ROUND:
        print("EP titles:")
        for EP_entry in entries_list:
            EP_entry.printGuessedEP()
        
        print("\nEP songs:")
        for EP_entry in entries_list:
            for entry in EP_entry.entry_list_unguessed:
                random_songs_list.append(entry)
        
        shuffle(random_songs_list)
        
        for entry in random_songs_list:
            entry.printEntry()

    else:
        for entry in entries_list:
            entry.printEntry()


def printGuessedLetters(guessed_letters):

    """Helps to keep track of what's been guessed."""

    print("\nGuessed letters: ", end="")

    for letter in guessed_letters:
        print(letter.upper(), end=" ")


def testing(entries_list):
    # Testing
    if IS_EP_ROUND:
        print(entries_list)
        for i in entries_list:
            print("?:", i.blank_EP_name)
    
            for j in i.entry_list_unguessed:
                print(j.artist, "-", j.song)
            
            print()    


def main():
    LIST_NAME = askForName()

    # Put this somewhere else later
    # also consider making this only once and save all the
    # guesses and such in a JSON to make it easier to load

    if input("Is this an EP round? (y/n): ") == 'y':
        global IS_EP_ROUND
        IS_EP_ROUND = True

    entries_list = []
    entries_list = loadSongs(LIST_NAME, entries_list)
    
    guessed_letters = []
    guessed_words = []

    saveBlankNames(entries_list)
    
    testing(entries_list)
    
    loadGuessesFile(LIST_NAME, entries_list, guessed_letters, guessed_words)
    loadGuessedPlayers(LIST_NAME, entries_list)
    
    random_songs_list = []
    printBlankList(entries_list, random_songs_list)
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





# Main program
main()
