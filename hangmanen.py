class Hangmanen():
    """Modified hangman with multiple phrases as entries. Originaly designed for
    use on DTForums' roulette games."""
    
    def __init__(self):
        self.list_name = "test.txt"
        self.names = []
        self.blank_names = []
    
    
    def askForNames(self):
        
        """Prompts the user to enter the name of the list containing the names."""
        
        pass
    
    
    def loadNames(self):
        
        """Loads the list of names from a text file, one per line."""
        
        with open(self.list_name, "r", encoding='utf-8') as file:
            
            for line in file:
                # Delete any extra space at the end
                line = line.strip()
                line = line.split(" - ", maxsplit = 1)

                # Separates artist and song name
                self.names.append(line)
                
        print(self.names) # Just for testing
        #for i in self.names:
            #print(i)
    
    
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
            print("Choose one: \n",
                  "1. Guess a word. \n",
                  "2. Guess a leter. \n")
            
            choice = int(input())
            
            if choice != 1 or choice != 2:
                print("Error, insert a valid number.")

            else:
                break
        
        return choice
    
    
    def replaceInList(self, wordOrLetter):
        
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
                        
                        # Iterates until the whole item is replaced in blank
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
        
        for name in self.blank_names:

            item_pos = 0

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
    

# Testing
drunk = Hangmanen()
drunk.loadNames()
drunk.createBlankNames()
print(drunk.checkComplete())
#drunk.askWordOrLetter()
drunk.replaceInList("a")
drunk.printBlankList()