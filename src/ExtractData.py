from MyExceptions import *
import csv
from Interval import Interval
from collections import defaultdict

"""This class extracts the informations of a file and store them in a triple hashmap."""
class ExtractData :
    
    def readAndExtract(self, filepath, dict_data, config_file_type):
        """Read the file and extract the meaningful informations depending on the type file.
        The extracted information is stored in a triple hashmap

        Attributes:
            filespath : the file array containing the files' path
            config_file_type : contains the informations on the file type (the extension, the important fields, etc...)
            dict_data : the triple hashmap
        """

        filename = filepath.split("/")[-1]
        
        #Open the file with the csv function
        with open(filepath, "r") as f:
            reader = csv.reader(f, delimiter=chr(int(config_file_type[1])))
            #For each line in the file, call the extract method
            for _, line in enumerate(reader):
                self.verify_length(line, config_file_type[2])
                dict_data = self.extract(dict_data, line, filename, config_file_type)

        """Return the updated triple hashmap with the right informations"""
        return dict_data
        
    def extract(self, dict_data, line, filename, config_file_type):
        """Store the meaningful informations of the line in an Interval object 
        and put it in the triple hashmap. Example with the paf file type :
            id_A :      line[0] 
            id_B :      line[5]
            length_A :  line[1]
            length_B :  line[6]
            start_A :   line[2]
            start_B :   line[7]
            end_A :     line[3]
            end_B :     line[8]
            strand :    line[4]

            Attributes:
            dict_data : the triple hashmap
                The method will add the Overlap informations of the line in this structure
            line : the information of the line (it's an string array)
            filename : the name of the file
            config_file_type : contains the informations on the file type (the extension, the important fields, etc...)
        """

        #Analyse the strand of the interval
        strand = ''
        if int(config_file_type[11]) == 1:
            strand = line[int(config_file_type[12])]
        else :
            strand_A = int(line[int(config_file_type[12])])
            strand_B = int(line[int(config_file_type[13])])
            if strand_A == strand_B:
                strand = '+'
            else:
                strand = '-'

        #Create an interval according to the config_file_type informations (which were in the allowed_files.csv file)
        tmp_interval = Interval(filename,
        int(line[int(config_file_type[3])]), int(line[int(config_file_type[4])]),
        strand,
        int(line[int(config_file_type[5])]), int(line[int(config_file_type[6])]), 
        int(line[int(config_file_type[7])]), int(line[int(config_file_type[8])]), 
        int(line[int(config_file_type[9])]), int(line[int(config_file_type[10])]))
        

        #if 'read A' not in dict_data
        #Create the second hashmap if the key is new        
        if line[int(config_file_type[3])] not in dict_data:
            dict_data[line[int(config_file_type[3])]] = {} 
        if line[int(config_file_type[4])] not in dict_data:
            dict_data[line[int(config_file_type[4])]] = {} 
        
        #if 'read B' not in dict_data[read A]
        #Create the third hashmap if the key is new
        if line[int(config_file_type[4])] not in dict_data[line[int(config_file_type[3])]]:
            dict_data[line[int(config_file_type[3])]][line[int(config_file_type[4])]] = {}
        if line[int(config_file_type[3])] not in dict_data[ line[int(config_file_type[4])]]:
            dict_data[line[int(config_file_type[4])]][line[int(config_file_type[3])]] = {}
        
        #if '+' not in dict_data[read A][read B]
        #Create the array if the interval is new in dict_data[read A][read B][+]
        if strand not in dict_data[line[int(config_file_type[3])]][line[int(config_file_type[4])]] :
            dict_data[line[int(config_file_type[3])]][line[int(config_file_type[4])]][strand] = []
        if strand not in dict_data[line[int(config_file_type[4])]][line[int(config_file_type[3])]] :
            dict_data[line[int(config_file_type[4])]][line[int(config_file_type[3])]][strand] = []
        
        #Add the interval in the triple hashmap
        dict_data[line[int(config_file_type[3])]][line[int(config_file_type[4])]][strand].append(tmp_interval)
        dict_data[line[int(config_file_type[4])]][line[int(config_file_type[3])]][strand].append(tmp_interval)
        
        return dict_data

    def verify_length(self, line, nb_fields):
        if len(line) != int(nb_fields):
            raise BadFormatFileError()

