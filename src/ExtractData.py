from MyExceptions import *
import csv
from Interval import Interval
from collections import defaultdict

"""This class extracts the informations of a file and store them in a double hashmap."""
class ExtractData :
    
    def readAndExtract(self, filepath, dictData, separator):
        """Read the file and extract the meaningful informations depending on the type file.
        The extracted information is stored in a double hashmap

        Attributes:
            filespath : the file array containing the files' path
            separator : the parsing delimiter for the csv function
            dictData : the double hashmap
        """

        filename = filepath.split("/")[-1]

        #Open the file with the csv function
        with open(filepath, "r") as f:
            reader = csv.reader(f, delimiter=separator)
            #For each line in the file, call the extract method
            for _, line in enumerate(reader):
                self.verify_length(line)
                dictData = self.extract(dictData, line, filename)
        
        """Return the updated double hashmap with the right informations"""
        return dictData
        
    def extract(self, dictData, line, filename):
        """This method is created to mimic the abstraction behaviour.
        This method, in this case, isn't destined to be called.

        Attributes:
            dictData : the double hashmap
                The method will add the Overlap informations of the line in this structure
            line : the information of the line (it's an string array)
            filename : the name of the file
        """
        raise NotImplementedMethodError

    def verify_length(self, line):
        raise NotImplementedMethodError

"""This class extracts the informations of a PAF file and store them in a double hashmap."""
class ExtractDataPaf(ExtractData):
    def extract(self, dictData, line, filename):
        """Store the meaningful informations of the line in an Interval object 
        and put it in the double hashmap.
            id_A >      line[0] 
            id_B >      line[5]
            length_A >  line[1]
            length_B >  line[6]
            start_A >   line[2]
            start_B >   line[7]
            end_A >     line[3]
            end_B >     line[8]

            Attributes:
            dictData : the double hashmap
                The method will add the Overlap informations of the line in this structure
            line : the information of the line (it's an string array)
            filename : the name of the file
        """
        
        tmp_interval = Interval(filename, line[0], line[5], 
        line[1], line[6], line[2], line[7], line[3], line[8])

        #Create the second hashmap if the key is new        
        if line[0] not in dictData:
            dictData[line[0]] = {} 
        if line[5] not in dictData:
            dictData[line[5]] = {} 
        
        #Create the array if the interval is new
        if line[5] not in dictData[line[0]]:
            dictData[line[0]][line[5]] = []
        if line[0] not in dictData[line[5]]:
            dictData[line[5]][line[0]] = []
        

        #default_dict
        #Add the interval in the double hashmap
        dictData[line[0]][line[5]].append(tmp_interval)
        dictData[line[5]][line[0]].append(tmp_interval)
        #print('line[{}] = {}'.format(i, line))
        
        return dictData

    def verify_length(self, line):
        if len(line) != 16:
            raise BadFormatFileError()

"""This class extracts the informations of a MHAP file and store them in a double hashmap."""
class ExtractDataMhap(ExtractData):
    def extract(self, dictData, line, filename):
        """Store the meaningful informations of the line in an Interval object 
        and put it in the double hashmap.
            id_A >      line[0] 
            id_B >      line[1]
            length_A >  line[7]
            length_B >  line[11]
            start_A >   line[5]
            start_B >   line[9]
            end_A >     line[6]
            end_B >     line[10]

            Attributes:
            dictData : the double hashmap
                The method will add the Overlap informations of the line in this structure
            line : the information of the line (it's an string array)
            filename : the name of the file
        """
        tmp_interval = Interval(filename, line[0], line[1], 
        line[7], line[11], line[5], line[9], line[6], line[10])
        
        #Create the second hashmap if the key is new
        if line[0] not in dictData:
            dictData[line[0]] = {} 
        if line[1] not in dictData:
            dictData[line[1]] = {} 
        
        if line[1] not in dictData[line[0]]:
            dictData[line[0]][line[1]] = []
        if line[0] not in dictData[line[1]]:
            dictData[line[1]][line[0]] = []

        #Add the interval in the double hashmap
        dictData[line[0]][line[1]].append(tmp_interval)
        dictData[line[1]][line[0]].append(tmp_interval)
        #print('line[{}] = {}'.format(i, line))

        
        return dictData
    
    def verify_length(self, line):
        if len(line) != 12:
            raise BadFormatFileError()