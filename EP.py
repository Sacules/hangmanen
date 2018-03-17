class EP():
    
    """Simple container for several entries."""
    
    def __init__(self):
        
        self.entry_list = []
        self.player = ""
        self.name = ""
        self.blank_name = ""
    
    def loadEntry(self, entry):
        self.entry_list.append(entry)
        