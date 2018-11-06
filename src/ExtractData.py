from MyExceptions import *
import csv
from Interval import Interval
from collections import defaultdict

"""This class extracts the informations of a file and store them in a double hashmap."""
class ExtractData :
    
    def readAndExtract(self, filepath, dict_data, config_file_type):
        """Read the file and extract the meaningful informations depending on the type file.
        The extracted information is stored in a double hashmap

        Attributes:
            filespath : the file array containing the files' path
            config_file_type : contains the informations on the file type (the extension, the important fields, etc...)
            dict_data : the double hashmap
        """

        filename = filepath.split("/")[-1]
        
        #Open the file with the csv function
        with open(filepath, "r") as f:
            reader = csv.reader(f, delimiter=chr(int(config_file_type[1])))
            #For each line in the file, call the extract method
            for _, line in enumerate(reader):
                self.verify_length(line, config_file_type[2])
                dict_data = self.extract(dict_data, line, filename, config_file_type)

        """Return the updated double hashmap with the right informations"""
        return dict_data
        
    def extract(self, dict_data, line, filename, config_file_type):
        """Store the meaningful informations of the line in an Interval object 
        and put it in the double hashmap. Example with the paf file type :
            id_A >      line[0] 
            id_B >      line[5]
            length_A >  line[1]
            length_B >  line[6]
            start_A >   line[2]
            start_B >   line[7]
            end_A >     line[3]
            end_B >     line[8]

            Attributes:
            dict_data : the double hashmap
                The method will add the Overlap informations of the line in this structure
            line : the information of the line (it's an string array)
            filename : the name of the file
            config_file_type : contains the informations on the file type (the extension, the important fields, etc...)
        """

        #Create an interval according to the config_file_type informations (which were in the allowed_files.csv file)
        tmp_interval = Interval(filename, 
        line[int(config_file_type[3])], line[int(config_file_type[4])],
        line[int(config_file_type[5])], line[int(config_file_type[6])], 
        line[int(config_file_type[7])], line[int(config_file_type[8])], 
        line[int(config_file_type[9])], line[int(config_file_type[10])])
        
        #Create the second hashmap if the key is new        
        if line[int(config_file_type[3])] not in dict_data:
            dict_data[line[int(config_file_type[3])]] = {} 
        if line[int(config_file_type[4])] not in dict_data:
            dict_data[line[int(config_file_type[4])]] = {} 
        
        #Create the array if the interval is new
        if line[int(config_file_type[4])] not in dict_data[line[int(config_file_type[3])]]:
            dict_data[line[int(config_file_type[3])]][line[int(config_file_type[4])]] = []
        if line[int(config_file_type[3])] not in dict_data[ line[int(config_file_type[4])]]:
            dict_data[line[int(config_file_type[4])]][line[int(config_file_type[3])]] = []
        
        #Add the interval in the double hashmap
        dict_data[line[int(config_file_type[3])]][line[int(config_file_type[4])]].append(tmp_interval)
        dict_data[line[int(config_file_type[4])]][line[int(config_file_type[3])]].append(tmp_interval)
        
        return dict_data

    def verify_length(self, line, nb_fields):
        if len(line) != int(nb_fields):
            raise BadFormatFileError()

