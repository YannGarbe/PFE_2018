import csv
from Interval import Interval

class ReadFiles:

    def ReadAllFiles(self, filespath):
        """Read each files in given the file array and store it on a dictionnary

        Attributes:
            filespath : the file array containing the files' path
        """
        dictData = {}
        tmp_data = []
        filename = ""
        for filepath in filespath:
            filename = filepath.split("/")[-1]
            tmp_data = self.ReadAFile(filepath)

            dictData[filename] = tmp_data

        """Return the dictionnary containing the data of all the files"""
        return dictData

    def ReadAFile(self, filepath):
        """Read a 'hisea', 'paf' or 'mhap' file and store its data on a 2 dimensions array
        
        
        Attributes:
            filepath : the file's path
        """
        extension = filepath.split('.')[-1]
        data = []
        
        
        file = open (filepath, "r")
        for line in file:
            data_line = []
            on_word = False
            word = ""

            line = line.replace("\t", " ")

            for c in line:
                if c != ' ':
                    word = word + c
                    on_word = True
                elif c == ' ' and on_word:
                    data_line.append(word)
                    word = ""
                    on_word = False
            data_line.append(word[:-1])
            data.append(data_line)
        
        """Return the array containing the file's data"""
        return data

        #Créer une classe qui garde les informations importantes
        #Table de hash qui avec A > Tous les overlaps de 
        #Table [Read A] [Read B] > Objet contenant l'overlap
        # table[Read B][Read A] = table[Read A][Read B]
        
        #Fonction de hash
        # "1" -> 56
        # "2" -> 56 => Collision, du coup python duplique la valeur

        # =>> Le nombre d'opérations dans une table 

    def ExtractHiseaData(self, filepath):
        """Extract the right informations in a hisea file and store it in an object

        Attributes:
            filepath : the file's path
        """
        pass
    
    def ExtractPafData(self, filepath):
        """Extract the right informations in a paf file and store it in an object

        Attributes:
            filepath : the file's path
        """
        dictData = {}

        filename = filepath.split("/")[-1]

        with open(filepath, "r") as f:
            reader = csv.reader(f, delimiter="\t")
            for i, line in enumerate(reader):
                """
                    id_A >      line[0] 
                    id_B >      line[5]
                    start_A >   line[2]
                    start_B >   line[7]
                    end_A >     line[3]
                    end_B >     line[8]
                """
                tmp_interval = Interval(filename, line[0], line[5], line[2], line[7], 
                line[3], line[8])
                #print('line[{}] = {}'.format(i, line))


                
                if line[0] not in dictData:
                    dictData[line[0]] = {} 
                if line[5] not in dictData:
                    dictData[line[5]] = {} 
                
                #To fix?
                dictData[line[0]][line[5]] = tmp_interval
                dictData[line[5]][line[0]] = tmp_interval
                #print('line[{}] = {}'.format(i, line))

            print(dictData['2']['77893'].toStringInterval())
            print(dictData['77893']['2'].toStringInterval())
            
            return dictData
    
    def ExtractMhapData(self, filepath):
        """Extract the right informations in a mhap file and store it in an object

        Attributes:
            filepath : the file's path
        """
        dictData = {}

        filename = filepath.split("/")[-1]

        with open(filepath, "r") as f:
            reader = csv.reader(f, delimiter=" ")
            for i, line in enumerate(reader):
                """
                    id_A >      line[0] 
                    id_B >      line[1]
                    start_A >   line[5]
                    start_B >   line[9]
                    end_A >     line[6]
                    end_B >     line[10]
                """
                tmp_interval = Interval(filename, line[0], line[1], 
                line[5], line[9], line[6], line[10])
                
                if line[0] not in dictData:
                    dictData[line[0]] = {} 
                if line[1] not in dictData:
                    dictData[line[1]] = {} 
                
                #To fix?
                dictData[line[0]][line[1]] = tmp_interval
                dictData[line[1]][line[0]] = tmp_interval
                #print('line[{}] = {}'.format(i, line))

            print(dictData['11']['4182'].toStringInterval())
            print(dictData['4182']['11'].toStringInterval())
            
            return dictData