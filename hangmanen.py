"""
Modified hangman with multiple songs as entries. Originaly designed for
use on DTForums' roulette games.
"""

# ----- Modules ----- #
import Entry


# ----- Constants ----- #
LIST_NAME = ""


# ----- Functions ----- #
def askListName():
    print("Name of the text file to load (without the extension): ", end="")
    global LIST_NAME
    LIST_NAME = input()


def loadSongs():

    """Reads the entries from a text file, one per line."""

    while True:
        try:
            file = open(LIST_NAME + ".txt", "r", encoding='utf-8')

        except FileNotFoundError:
            print("Error! File not found. Please enter name again.")
            askListName()

        else:
            break

    entries_list = []

    for line in file:
        # line = "Player: Artist - Song\n"
        line = line.strip()

        # line = ["Player", "Artist - Song"]
        line = line.split(": ", maxsplit=1)
        entry = Entry(line[1], line[0])

        entries_list.append(entry)

    return entries_list


def validLetter(entries_list, guess):

    """ Checks if the letter exists on any of the entries. """

    guess_lower = guess.lower()
    guess_upper = guess.upper()

    for entry in entries_list:
        # The letter has to be checked in both
        # lowercase and uppercase
        if guess_lower in entry.name or guess_upper in entry.name:
            return True

    return False


def validWord(entries_list, guess):

    """
    This assumes you're writing the words exactly as they written in
    the entries. No spellchecking, this is case-sensitive.
    """

    for entry in entries_list:
        if guess in entry.name:
            return True

    return False


def checkGoodGuess(entries_list, guess, guessed_letters, guessed_words):

    """
    It is important to separate what kind of guess the player is
    giving and save the correct ones.
    """

    while guess in guessed_letters or guess in guessed_words:
        print("\nGuess is already existing. Try another one.")
        guess = input("New guess: ")

    if len(guess) == 1:
        return validLetter(entries_list, guess)

    if len(guess) > 1:
        return validWord(entries_list, guess)


def saveGoodGuess(entries_list, guess, guessed_letters, guessed_words):
    if checkGoodGuess(entries_list, guess, guessed_letters, guessed_words):
        for entry in entries_list:
            if len(guess) == 1:
                entry.replaceLetter(guess.lower())
                entry.replaceLetter(guess.upper())
                guessed_letters.append(guess)

            if len(guess) > 1:
                entry.replaceWord(guess)
                guessed_words.append(guess)

    return(guessed_letters, guessed_words)


def loadGuessesFile(entries_list, guessed_letters, guessed_words):

    """Reads saved guesses from a text file."""

    try:
        file = open(LIST_NAME + ' guesses.txt', 'r', encoding='utf-8')

    except FileNotFoundError:
        file = open(LIST_NAME + ' guesses.txt', 'w', encoding='utf-8')

    finally:
        for line in file:
            line = line.strip()

            if "\ufeff" in line:
                line = line.replace("\ufeff", "")

            guessed_letters, guessed_words = checkGoodGuess(entries_list,
                                                        line,
                                                        guessed_letters,
                                                        guessed_words)

        file.close()

    return (guessed_letters, guessed_words)


def askGuess():

    guess = input("Enter a word or letter to guess: ")

    return guess


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


def saveGuess(guess):

    """Puts them in a text file to be loaded later."""

    with open(LIST_NAME + ' guesses.txt', 'a', encoding='utf-8') as file:
        file.write(guess + '\n')


def saveGuessedPlayer(player):

    """Same as above, but separate from it."""

    with open(LIST_NAME + " guessed players.txt",
              "a", encoding="utf-8") as file:

        file.write(player + '\n')


def loadGuessedPlayers(entries_list):

    """Reads from a file then modifies the entry objects if it exists."""

    try:
        file = open(LIST_NAME + ' guessed players.txt', 'r', encoding='utf-8')

    except FileNotFoundError:
        file = open(LIST_NAME + ' guessed players.txt', 'w', encoding='utf-8')

    finally:
        for line in file:
            line = line.strip()
            guessedPlayer(entries_list, line)

        file.close()


def guessedPlayer(entries_list, player):

    """
       Looks for the the player and makes it printable once it's
       been guessed.
    """

    for entry in entries_list:
        if entry.player == player:
            entry.guessed_player = True #TODO: Put this in a method


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
    askListName()
    entries_list = loadSongs()

    guessed_letters = []
    guessed_words = []
    guessed_letters, guessed_words = loadGuessesFile(entries_list,
                                                     guessed_letters,
                                                     guessed_words)
    loadGuessedPlayers(entries_list)

    printBlankList(entries_list)
    printGuessedLetters(guessed_letters)

    while not checkComplete(entries_list):
        choice = promptUser()

        if choice == "1":
            guess = askGuess()
            guessed_entries = checkGoodGuess(entries_list, guess,
                                         guessed_letters, guessed_words)
            guessed_letters = guessed_entries[0]
            guessed_words = guessed_entries[1]

            if guess in guessed_letters or guess in guessed_words:
                saveGuess(guess)

        elif choice == "2":
            player = input("Write the name of the guessed player: ")
            guessedPlayer(entries_list, player)
            saveGuessedPlayer(player)

        elif choice == "3":
            break

        printBlankList(entries_list)
        printGuessedLetters(guessed_letters)


#----- Main Program -----#
if __name__ == "__main__":
    main()
