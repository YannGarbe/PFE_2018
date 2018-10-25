import csv
from Interval import Interval
from ExtractData import *
from MyExceptions import NotYetImplementedError

"""This class reads the different files and store their information"""
class ReadFiles:

    def readAllFiles(self, filespath):
        """Read each files in given the file array and store it in a dictionnary

        Attributes:
            filespath : the file array containing the files' path
        """
        dict_all_files_data = {}
        tmp_data = {}
        filename = ""
        for filepath in filespath:
            filename = filepath.split("/")[-1]
            tmp_data = self.readAFile(filepath)

            dict_all_files_data[filename] = tmp_data

        """Return the dictionnary containing the data of all the files"""
        return dict_all_files_data

    def readAFile(self, filepath):
        """Read a 'hisea', 'paf' or 'mhap' file and store its data 
        in a double hashmap (dictionnary in python)
        
        
        Attributes:
            filepath : the file's path
        """
        extension = filepath.split(".")[-1]
        dictData = {}

        #Check the file's extension
        if(extension == "paf"):
            #If it's a paf file, do the proper extraction
            dictData = ExtractDataPaf().readAndExtract(filepath, "\t")
            
            print(dictData['2']['77893'].toStringInterval())
            print(dictData['77893']['2'].toStringInterval())
            
            return dictData
        elif(extension == "mhap"):
            #If it's a mhap file, do the proper extraction
            dictData = ExtractDataMhap().readAndExtract(filepath, " ")
            
            print(dictData['11']['4182'].toStringInterval())
            print(dictData['4182']['11'].toStringInterval())
            
            return dictData
        else:
            raise NotYetImplementedError()
            

        #Créer une classe qui garde les informations importantes
        #Table de hash qui avec A > Tous les overlaps de 
        #Table [Read A] [Read B] > Objet contenant l'overlap
        # table[Read B][Read A] = table[Read A][Read B]
        
        #Fonction de hash
        # "1" -> 56
        # "2" -> 56 => Collision, du coup python duplique la valeur

        # =>> Le nombre d'opérations dans une table 