from MyExceptions import NotImplementedMethodError
import csv
from Interval import Interval

"""This class extracts the informations of a file and store them in a double hashmap."""
class ExtractData :
    
    def readAndExtract(self, filepath, separator):
        """Read the file and extract the meaningful informations depending on the type file.
        The extracted information is stored in a double hashmap

        Attributes:
            filespath : the file array containing the files' path
            separator : the parsing delimiter for the csv function
        """
        dictData = {}

        filename = filepath.split("/")[-1]

        #Open the file with the csv function
        with open(filepath, "r") as f:
            reader = csv.reader(f, delimiter=separator)
            #For each line in the file, call the extract method
            for _, line in enumerate(reader):
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
    

"""This class extracts the informations of a PAF file and store them in a double hashmap."""
class ExtractDataPaf(ExtractData):
    def extract(self, dictData, line, filename):
        """Store the meaningful informations of the line in an Interval object 
        and put it in the double hashmap.
            id_A >      line[0] 
            id_B >      line[5]
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
        
        tmp_interval = Interval(filename, line[0], line[5], line[2], line[7], 
        line[3], line[8])

        #Create the second hashmap if the key is new        
        if line[0] not in dictData:
            dictData[line[0]] = {} 
        if line[5] not in dictData:
            dictData[line[5]] = {} 
        
        #To fix?
        dictData[line[0]][line[5]] = tmp_interval
        dictData[line[5]][line[0]] = tmp_interval
        #print('line[{}] = {}'.format(i, line))
        
        return dictData

"""This class extracts the informations of a MHAP file and store them in a double hashmap."""
class ExtractDataMhap(ExtractData):
    def extract(self, dictData, line, filename):
        """Store the meaningful informations of the line in an Interval object 
        and put it in the double hashmap.
            id_A >      line[0] 
            id_B >      line[1]
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
        line[5], line[9], line[6], line[10])
        
        #Create the second hashmap if the key is new
        if line[0] not in dictData:
            dictData[line[0]] = {} 
        if line[1] not in dictData:
            dictData[line[1]] = {} 
        
        #To fix?
        dictData[line[0]][line[1]] = tmp_interval
        dictData[line[1]][line[0]] = tmp_interval
        #print('line[{}] = {}'.format(i, line))

        
        return dictData