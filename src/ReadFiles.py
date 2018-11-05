import csv
from Interval import Interval
from ExtractData import *
from MyExceptions import NotYetImplementedError

"""This class reads the different files and store their information"""
class ReadFiles:

    def readAllFiles(self, filespath):
        """Read each files in given the file array and store it in a double hashmap

        Attributes:
            filespath : the file array containing the files' path
        """
        dictData = {}

        
        
        for filepath in filespath:
            tmp_data = self.readAFile(filepath, dictData)

        """Return the double hashmap containing the data of all the files"""
        return dictData

    def readAFile(self, dictData, filepath):
        """Read a 'hisea', 'paf' or 'mhap' file and store its data 
        in a double hashmap (dictionnary in python)
        
        
        Attributes:
            filepath : the file's path
            dictData : the double hashmap
        """
        extension = filepath.split(".")[-1]
        
        #Check the file's extension
        if(extension == "paf"):
            #If it's a paf file, do the proper extraction
            dictData = ExtractDataPaf().readAndExtract(filepath, dictData, "\t")
            
            print(dictData['2']['77893'][0].toStringInterval())
            print(dictData['77893']['2'][0].toStringInterval())
            
            
            return dictData
        elif(extension == "mhap"):
            #If it's a mhap file, do the proper extraction
            dictData = ExtractDataMhap().readAndExtract(filepath, dictData, " ")
            
            print(dictData['11']['4182'])
            print(dictData['4182']['11'])
            
            return dictData
        else:
            raise NotYetImplementedError()
