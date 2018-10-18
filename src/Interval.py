
"""This class store the overlap informations between two reads, A and B"""
class Inverval :

    def __init__(self, filename, id_A, id_B, reverse_A, 
    reverse_B, start_A, start_B, end_A, end_B):
        """Initiate the class with the given informations
        
        
        Attritbutes:
            filename : the name of the file
            id_A : the id of the Read A
            id_B : the id of the Read B
            reverse_A : False if the Read A sequence isn't reversed, True if it is
            reverse_B : False if the Read B sequence isn't reversed, True if it is
            start_A : the start index of the Read A overlapped sequence
            start_B : the start index of the Read B overlapped sequence
            end_A : the end index of the Read A overlapped sequence
            end_B : the end index of the Read B overlapped sequence
        """
        self.filename = filename

        self.id_A = id_A
        self.id_B = id_B
        
        self.reverse_A = reverse_A
        self.reverse_B = reverse_B
        
        self.start_A = start_A
        self.start_B = start_B

        self.end_A = end_A
        self.end_B = end_B

    #===========================Getters========================================
    
    def getFilename(self):
        return self.filename
    
    #---------------------------

    def getId_A(self):
        return self.id_A

    def getId_B(self):
        return self.id_B

    #---------------------------

    def getReverse_A(self):
        return self.reverse_A

    def getReverse_B(self):
        return self.reverse_B

    #---------------------------

    def getStart_A(self):
        return self.start_A
    
    def getStart_B(self):
        return self.start_B

    #---------------------------

    def getEnd_A(self):
        return self.end_A
    
    def getEnd_B(self):
        return self.end_B

    