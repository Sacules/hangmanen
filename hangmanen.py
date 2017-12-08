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
                
                # Separates artist and song name
                self.names.append(line.split(" - ", maxsplit = 1))
                
        print(self.names) # Just for testing
        #for i in self.names:
            #print(i)
    
    
    def createBlankNames(self):
        
        """Based on the names loaded, creates the blanks for the player to
        guess. They're saved in a text file."""
        
        for name in self.names:
            
            new_name = []
            
            for item in name:
                
                new_item = ""
                
                for letter in item:
                    
                    if letter == " ":
                        new_item = new_item + " "
                    
                    elif letter == "-":
                        new_item = new_item + "-"
                        
                    else:
                        new_item = new_item + "_"
                
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
    
    def isThereWord(self, word):
        
        """Checks if the word guessed is in the list."""
        
        for name in self.names:
            
            for item in name:
                
                if word in item:
                    return True
        
        return False





# Testing
drunk = Hangmanen()
drunk.loadNames()
drunk.createBlankNames()
print(drunk.checkComplete())
drunk.askWordOrLetter()
drunk.isThereWord("earth day")