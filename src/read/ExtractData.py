import csv
import pandas as pd
from collections import defaultdict
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from misc.Interval import Interval
from misc.MyExceptions import *

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
        
        cpt = 0
        #Open the file with the csv function
        """
        with open(filepath, "r") as f:
            reader = csv.reader(f, delimiter=chr(int(config_file_type[1])))
            #For each line in the file, call the extract method
            
            for _, line in enumerate(reader):
                print(cpt)
                cpt = cpt+1
            
                self.verify_length(line, config_file_type[2], filename)
                dict_data = self.extract(dict_data, line, filename, config_file_type)
        """
        for df in pd.read_csv(filepath,sep=chr(int(config_file_type[1])), header = None, chunksize=1):
            dict_data = self.extract(dict_data, df, filename, config_file_type)
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

        #Retrieve values
        data_id_a = str(line[int(config_file_type[3])].values[0])
        data_id_b = str(line[int(config_file_type[4])].values[0])
        
        data_length_A = str(line[int(config_file_type[5])].values[0]) #5
        data_length_B = str(line[int(config_file_type[6])].values[0]) #6

        data_start_A = str(line[int(config_file_type[7])].values[0]) #7
        data_start_B = str(line[int(config_file_type[8])].values[0]) #8    
        data_end_A = str(line[int(config_file_type[9])].values[0])   #9
        data_end_B = str(line[int(config_file_type[10])].values[0])  #10
        
        

        
        #Analyse the strand of the interval
        strand = ''
        if int(config_file_type[11]) == 1:
            strand = line[int(config_file_type[12])].values[0]
        else :
            strand_A = int(line[int(config_file_type[12])].values[0])
            strand_B = int(line[int(config_file_type[13])].values[0])
            if strand_A == strand_B:
                strand = '+'
            else:
                strand = '-'
        
        
        #Create an interval according to the config_file_type informations (which were in the allowed_files.csv file)
        tmp_interval = Interval(filename,
        int(data_id_a), int(data_id_b),
        strand,
        int(data_length_A), int(data_length_B), 
        int(data_start_A), int(data_start_B), 
        int(data_end_A), int(data_end_B))
        
        #If there are any entries in dict_data[id_b][id_a][strand], put it in there. Otherwise, put the interval in dict_data[id_a][id_b][strand]
        if (data_id_b in dict_data) and (data_id_a in dict_data[data_id_b]) and (strand in dict_data[data_id_b][data_id_a]):
            dict_data[data_id_b][data_id_a][strand].append(tmp_interval)
        else:
            #if 'read A' not in dict_data
            #Create the second hashmap if the key is new        
            if data_id_a not in dict_data:
                dict_data[data_id_a] = {} 
            
            #if 'read B' not in dict_data[read A]
            #Create the third hashmap if the key is new
            if data_id_b not in dict_data[data_id_a]:
                dict_data[data_id_a][data_id_b] = {}
            
            #if '+' not in dict_data[read A][read B]
            #Create the array if the interval is new in dict_data[read A][read B][+]
            if strand not in dict_data[data_id_a][data_id_b] :
                dict_data[data_id_a][data_id_b][strand] = []
            
            #Add the interval in the triple hashmap
            dict_data[data_id_a][data_id_b][strand].append(tmp_interval)
        
        return dict_data

    def verify_length(self, line, nb_fields, filename):
        if len(line) < int(nb_fields):
            raise BadFormatFileError(filename + " : not enough fields.\nThe fields : " + str(line))

