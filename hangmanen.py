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
                line = line.strip() # Deletes any extra space at the end
                self.names.append(line.split(" - ", maxsplit = 1)) # Separates artist and song name
                
        print(self.names)
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
        pass
    
        







# Testing
drunk = Hangmanen()
drunk.loadNames()
drunk.createBlankNames()
                
                
                