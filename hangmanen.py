class Hangmanen():
    """Modified hangman with multiple phrases as entries. Originaly designed for
    use on DTForums' roulette games."""
    
    def __init__(self):
        self.list_name = "test.txt"
        self.names = []
        self.blank_names = []
        self.guessedLetters = []
        self.players = dict()
        self.guessedPlayers = []
    
    
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
            
            for line in file:
                
                # Delete any extra space at the end
                line = line.strip()
                
                # Separate player name and song in a temporary list
                temp = line.split(": ", maxsplit = 1)
                
                # Save player name in the dict
                self.players[temp[1]] = temp[0]
                
                # Save the song in the list
                line = temp[1].split(" - ", maxsplit = 1)

                # Separates artist and song name
                self.names.append(line)
                

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


    def loadGuessesFile(self):
        try:
            with open(self.list_name + ' guesses', 'r', encoding='utf-8') as file:
                for line in file:

                    line = line.strip()
                    
                    if len(line) == 1:
                        self.replaceInList(line.lower(), False)
                        self.replaceInList(line.upper(), True)

                    else:
                        self.replaceInList(line, False)
                    

        except FileNotFoundError:
            file = open(self.list_name + ' guesses', 'w', encoding='utf-8')
            file.close()


    def askGuess(self, wrong):
        guess = input("Enter a word or letter to guess: ")
        
        if len(guess) == 1:
            wrong += self.replaceInList(guess.lower(), False)
            wrong += self.replaceInList(guess.upper(), True)
        
        else:
            wrong += self.replaceInList(guess, False)

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
                  "2. Show guessed player \n",
                  "3. Exit. \n")
            
            choice = input("Choose one: ")
            choice = int(choice)
            
            if choice != 1 and choice != 2 and choice != 3:
                print("Error, insert a valid number.")

            else:
                break
        
        return choice


    def saveGuess(self, guess):

        """Puts them in a text file to be loaded later."""

        with open(self.list_name + ' guesses', 'a', encoding='utf-8') as file:
            file.write(guess + '\n')


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
    
    
    def printBlankList(self):
        
        """Kinda obvious isn't it?"""
        
        # A little something to help me print the player names
        i = 0
        
        for name in self.blank_names:

            item_pos = 0

            # When we have guessed a player
            if name == self.names[i]:
                if self.players[name] in guessedPlayers:
                    print(self.players[name],  end=" ")

            else:
                print("?:", end=" ")
            
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

            # Moves to the next name in the original list
            i += 1
        
        # New line at the end
        print()
    
    
    def printGuessedLetters(self):
        
        """Magic."""
        
        print("Guessed letters: ", end="")
        
        for letter in self.guessedLetters:
            print(letter.upper(), end=" ")
        
        print()
    

    def askPlayerGuess(self):
        guess = input("\nEnter the name of the guessed player: ")

        self.guessedPlayers.append(guess)

        print(self.guessedPlayers)
        
        

# Testing
drunk = Hangmanen()
drunk.askForNames()
drunk.loadNames()
drunk.createBlankNames()
drunk.loadGuessesFile()
drunk.printBlankList()
drunk.printGuessedLetters()

while drunk.checkComplete() == False:
    wrong = 0    
    choice = drunk.askWordOrLetter()

    if choice == 1:
        drunk.askGuess(wrong)
        drunk.printBlankList()
        drunk.printGuessedLetters()

    if choice == 2:
        drunk.askPlayerGuess()
        drunk.printBlankList()
        drunk.printGuessedLetters()

    if choice == 3:
        break
    
        
