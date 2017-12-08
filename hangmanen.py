class Hangmanen():
    """Modified hangman with multiple phrases as entries. Originaly designed for
    use on DTForums' roulette games."""
    
    def __init__(self):
        self.list_name = "test.txt"
        self.names = []
        self.blank_names = []
        self.guessedLetters = []
        self.players = dict()
    
    
    def askForNames(self):
        
        """Prompts the user to enter the name of the list containing the names."""
        
        print("Name of the text file to load (without the extension): ",
              end="")
        
        self.list_name = input()
        print()
        self.list_name += ".txt"
    
    
    def loadNames(self):
        
        """Loads the list of names from a text file, one per line."""
        
        with open(self.list_name, "r", encoding='utf-8') as file:
            
            # Just something to keep track of players, useful later
            i = 0
            
            for line in file:
                
                # Delete any extra space at the end
                line = line.strip()
                
                # Separate player name and song in a temporary list
                temp = line.split(": ", maxsplit = 1)
                
                # Save player name in the dict
                self.players[i] = temp[0]
                
                # Save the song in the list
                line = temp[1].split(" - ", maxsplit = 1)

                # Separates artist and song name
                self.names.append(line)
                
                # Next player
                i += 1


    def createBlankNames(self):
        
        """Based on the names loaded, creates the blanks for the player to
        guess. They're saved in a text file."""
        
        for name in self.names:
            
            new_name = []
            
            for item in name:
                
                new_item = []
                
                for letter in item:
                    
                    if letter == " ":
                        new_item = new_item + [" "]
                    
                    elif letter == "-":
                        new_item = new_item + ["-"]
                        
                    else:
                        new_item = new_item + ["_"]
                
                new_name.append(new_item)
            
            self.blank_names.append(new_name)


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
            print(" 1. Guess a word or a letter. \n",
                   "2. Exit. \n")
            
            choice = input("Choose one: ")
            choice = int(choice)
            
            if choice != 1 and choice != 2:
                print("Error, insert a valid number.")

            else:
                break
        
        return choice
    
    
    def replaceInList(self, wordOrLetter, guessed):
        
        """Checks if the word or letter guessed is in the list. Then replaces
        it in the blank list."""
        
        # Initial name
        name_pos = 0
        
        # Will remain this if the word or letter isn't found
        noHangman = 0

        for name in self.names:
            
            # First check on band name
            item_pos = 0
            
            for item in name:
                
                char_pos = 0
                tail = 0
                
                if wordOrLetter in item:
                    
                    # No body part gets drawn
                    noHangman = 1
                    
                    # Letter
                    if len(wordOrLetter) == 1:
                        
                        if guessed == False:
                            self.guessedLetters.append(wordOrLetter)
                            guessed = True
                        
                        # Iterates until the whole letter is replaced in blank
                        while tail <= len(item):
                            
                            # Saves position
                            char_pos = item.find(wordOrLetter, tail)
                            
                            # If there is no letter in the substring
                            if char_pos == -1:
                                break
                            
                            # Replace it
                            self.blank_names[name_pos][item_pos][char_pos] = wordOrLetter
                            
                            # Take the substring after the first letter it finds
                            tail = char_pos + 1
                        
                    
                    # Word
                    else:
                        
                        # Get position
                        word_pos = item.find(wordOrLetter)
                        
                        for letter in wordOrLetter:
                            
                            # Replace one letter
                            self.blank_names[name_pos][item_pos][word_pos] = letter
                            
                            # Move on to the next one
                            word_pos += 1
                        

                # Switch to song name
                item_pos = 1

            # Switch to next name
            name_pos += 1
        
        return noHangman
    
    
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
    
    
    def printGuessedLetters(self):
        
        """Won't even bother to explain this."""
        
        print("Guessed letters: ", end="")
        
        for letter in self.guessedLetters:
            print(letter.upper(), end=" ")
        
        print()
    

# Testing
drunk = Hangmanen()
drunk.askForNames()
drunk.loadNames()
drunk.createBlankNames()

while drunk.checkComplete() == False:
    
    choice = drunk.askWordOrLetter()
    
    if choice == 2:
        break
    
    else:
        guess = input("Enter a word or letter to guess: ")
        
        if len(guess) == 1:
            drunk.replaceInList(guess.lower(), False)
            drunk.replaceInList(guess.upper(), True)
        
        else:
            drunk.replaceInList(guess, False)

        drunk.printBlankList(False)
        drunk.printGuessedLetters()
        