SPECIAL_CHARS = " -(),.:;?!'&"


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


def replaceLetter(ref_name, replacing_name, letter):

    """
    When a guessed letter is valid, all instances of it have
    to be replaced.
    """

    index_list = findIndexes(ref_name, letter)

    # Since strings are immutable, we need to transform it into a list
    replacing_name = list(replacing_name)

    if index_list != []:
        for index in index_list:
            replacing_name[index] = letter

    # We put it as a string back again
    return "".join(replacing_name)


def replaceWord(ref_name, replacing_name, word):

    """
    Replaces an instance of a word, or prompts for more if found.
    """

    index = ref_name.find(word)

    # Since strings are immutable, we need to transform these into lists
    replacing_name = list(replacing_name)
    word = list(word)

    for character in word:
        replacing_name[index] = character
        index += 1

    # We put it as a string back again
    return "".join(replacing_name)


def createBlankName(name):

    """
    Based on the names loaded, creates the blanks for the player to
    guess. They're saved in a text file.
    """

    new_name = ""

    for letter in name:
        index = SPECIAL_CHARS.find(letter)

        # The letter is no special character
        if index == -1:
            new_name = new_name + "_"

        else:
            new_name = new_name + SPECIAL_CHARS[index]

    return new_name