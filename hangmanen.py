class Hangmanen():
    """Modified hangman with multiple phrases as entries. Originaly designed for
    use on DTForums' roulette games."""
    
    def __init__(self):
        self.list_name = "test.txt"
        self.names = []
    
    def askForNames(self):
        """Prompts the user to enter the name of the list containing the names."""
        pass
    
    def loadNames(self):
        """Loads the list of names from a text file, one per line."""
        
        with open(self.list_name, "r", encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                self.names.append(line)
    
    def createBlankNames(self):
    
    def checkComplete(self):
        







# Testing
drunk = Hangmanen()
drunk.loadNames()
                
                
                