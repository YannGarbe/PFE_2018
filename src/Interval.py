
"""self class store the overlap informations between two reads, A and B"""


class Interval:

    def __init__(self, filename, id_A, id_B, strand,
    length_A, length_B, start_A, start_B, end_A, end_B):
        """Initiate the class with the given informations


        Attritbutes:
            filename : the name of the file
            id_A : the id of the Read A
            id_B : the id of the Read B
            strand : ‘+’ if query/target on the same strand; ‘-’ if opposite
            length_A : the length of A
            length_B : the length of B
            start_A : the start index of the Read A overlapped sequence
            start_B : the start index of the Read B overlapped sequence
            end_A : the end index of the Read A overlapped sequence
            end_B : the end index of the Read B overlapped sequence
        """
        self.filename = filename

        self.id_A = id_A
        self.id_B = id_B

        self.strand = strand

        self.length_A = length_A
        self.length_B = length_B

        self.start_A = start_A
        self.start_B = start_B

        self.end_A = end_A
        self.end_B = end_B

    # ===========================Getters========================================

    def getFilename(self):
        return self.filename

    # ---------------------------

    def getId_A(self):
        return self.id_A

    def getId_B(self):
        return self.id_B

    # ---------------------------

    def getStrand(self):
        return self.strand

    # ---------------------------

    def getLength_A(self):
        return self.length_A

    def getLength_B(self):
        return self.length_B

    # ---------------------------

    def getStart_A(self):
        return self.start_A

    def getStart_B(self):
        return self.start_B

    # ---------------------------

    def getEnd_A(self):
        return self.end_A

    def getEnd_B(self):
        return self.end_B

# ===========================Setters========================================

    def setFilename(self, filename):
        self.filename = filename

    # ---------------------------

    def setId_A(self, id_A):
        self.id_A = id_A

    def setId_B(self, id_B):
        self.id_B = id_B

    # ---------------------------

    def setStrand(self, strand):
        self.strand = strand

    # ---------------------------

    def setLength_A(self, length_A):
        self.length_A = length_A

    def setLength_B(self, length_B):
        self.length_B = length_B

    # ---------------------------

    def setStart_A(self, start_A):
        self.start_A = start_A

    def setStart_B(self, start_B):
        self.start_B = start_B

    # ---------------------------

    def setEnd_A(self, end_A):
        self.end_A = end_A

    def setEnd_B(self, end_B):
        self.end_B = end_B

    # ==============================================================

    def compareAndFusion_gentle(self, other_interval):
        # Tmp

        #if other_interval.getId_A() == 1 and other_interval.getId_B() == 6696:
        #    print(self.getEnd_A(), " VS ", other_interval.getStart_A(), " Du coup : ", self.getEnd_A() >= other_interval.getStart_A())
        
        
        if (self.getEnd_A() >= other_interval.getStart_A()) and (self.getStart_A() <= other_interval.getEnd_A()):

            if (self.getEnd_B() >= other_interval.getStart_B()) and (self.getStart_B() <= other_interval.getEnd_B()):

                self.setStart_A(
                min(self.getStart_A(), other_interval.getStart_A()))
                self.setStart_B(
                min(self.getStart_B(), other_interval.getStart_B()))

                self.setEnd_A(
                max(self.getEnd_A(), other_interval.getEnd_A()))
                self.setEnd_B(
                max(self.getEnd_B(), other_interval.getEnd_B()))
                return 1
            else:
                return 0
        else:
            return 0


    def compareAndFusion_strict(self, other_interval):
        # le but ici est, au lieu de vérifier et de fusionner au minimum en même temps,
        #    on ajoute l'interval à unifier dans un tableau, MAIS ON AJOUTE LE MAXIMUM ! Comme ça on peut être à peut prêt sur de prendre toutes les valeurs. 
        #    Une fois toutes les comparaisons faites, on fusionne le tout au minimal
        # 
        #if other_interval.getId_A() == 1 and other_interval.getId_B() == 6696:
        #    print(self.getEnd_A(), " VS ", other_interval.getStart_A(), " Du coup : ", self.getEnd_A() >= other_interval.getStart_A())
        
        
        if (self.getEnd_A() >= other_interval.getStart_A()) and (self.getStart_A() <= other_interval.getEnd_A()):

            if (self.getEnd_B() >= other_interval.getStart_B()) and (self.getStart_B() <= other_interval.getEnd_B()):

                self.setStart_A(
                min(self.getStart_A(), other_interval.getStart_A()))
                self.setStart_B(
                min(self.getStart_B(), other_interval.getStart_B()))

                self.setEnd_A(
                max(self.getEnd_A(), other_interval.getEnd_A()))
                self.setEnd_B(
                max(self.getEnd_B(), other_interval.getEnd_B()))
                return 1
            else:
                return 0
        else:
            return 0

    def equalsAndFusion_strict(self, other_interval):
        if (self.getEnd_A() >= other_interval.getStart_A()) and (self.getStart_A() <= other_interval.getEnd_A()):

            if (self.getEnd_B() >= other_interval.getStart_B()) and (self.getStart_B() <= other_interval.getEnd_B()):
                if (self.getFilename() == other_interval.getFilename()):
                    self.setStart_A(
                    min(self.getStart_A(), other_interval.getStart_A()))
                    self.setStart_B(
                    min(self.getStart_B(), other_interval.getStart_B()))

                    self.setEnd_A(
                    max(self.getEnd_A(), other_interval.getEnd_A()))
                    self.setEnd_B(
                    max(self.getEnd_B(), other_interval.getEnd_B()))
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0


    # ============================================================== 

    def toStringInterval(self):
        return ""+self.filename+": [id_A] : "+str(self.id_A)+"| [id_B] : "+str(self.id_B) + \
        "| [Strand] : "+str(self.strand)+"| [Length_B] : "+str(self.length_B) + \
        "| [Length_A] : "+str(self.length_A)+"| [Length_B] : "+str(self.length_B) + \
        "| [Start_A] : "+str(self.start_A)+"| [Start_B] : "+str(self.start_B) + \
        "| [End_A] : "+str(self.end_A)+"| [End_B] : "+str(self.end_B)
