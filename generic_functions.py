def askForName():

    """A simple user prompt."""

    print("Name of the text file to load (without the extension): ", end="")

    LIST_NAME = input()

    return LIST_NAME


def findIndexes(word, letter):

    """
    Iterates over a word and returns a list with the positions in
    which a letter apears on it.
    """

    index = 0
    index_list = []

    for character in word:
        if character == letter:
            index_list.append(index)

        index += 1

    return index_list


def replaceLetter(name, letter, replacing_name):

    """
    When a guessed letter is valid, all instances of it have
    to be replaced.
    """

    index_list = findIndexes(name, letter)

    # Since strings are immutable, we need to transform it into a list
    replacing_name = list(replacing_name)

    if index_list != []:
        for index in index_list:
            replacing_name[index] = letter

    # We put it as a string back again
    return "".join(replacing_name)


def replaceWords(replacing_name, guess, index):

    """
    Assume this won't go out of index range. Please.
    """

    replacing_name = list(replacing_name)
    guess = list(guess)

    for character in guess:
        replacing_name[index] = character
        index += 1
    
    return "".join(replacing_name)


def createBlankName(name):

    """
    Based on the names loaded, creates the blanks for the player to
    guess. They're saved in a text file.
    """

    new_name = ""
    special_chars = " -(),.:;?!'&"
    
    for letter in name:
        index = special_chars.find(letter)
        
        # When the letter is no special character
        if index == -1:
            new_name = new_name + "_"
        
        else:
            new_name = new_name + special_chars[index]

    return new_name


def isLetter(words):

    """
    This looks nicer and more understandable instead of just 
    using a '==' comparison.
    """

    return len(words) == 1


def askGuess():
    
    """Water is wet."""
    
    guess = input("Enter a word or letter to guess: ")
    
    return guess


