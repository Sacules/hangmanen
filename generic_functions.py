def askForName():

    """A simple user prompt."""

    print("Name of the text file to load (without the extension): ", end="")

    LIST_NAME = input()

    return LIST_NAME


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


