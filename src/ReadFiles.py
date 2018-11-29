import csv
import os.path
from Interval import Interval
from ExtractData import *
from MyExceptions import NotYetImplementedError

"""This class reads the different files and store their information"""
class ReadFiles:

    def readAllFiles(self, filespath, config_filepath):
        """Read each files in given the file array and store it in a triple hashmap

        Attributes:
            filespath : the file array containing the files' path
            config_filepath : the filepath of the file describing the allowed extensions
        """
        dict_data = {}

        config_data = []
        #Check if the config file type exists
        if not(os.path.isfile(config_filepath)):
            raise FileNotFoundError(config_filepath + " : Not Found")
        
        #Open it with csv module 
        with open(config_filepath, "r") as f_config:
            reader = csv.reader(f_config, delimiter=",")
            #For each line, store it in the config_data
            for _, line in enumerate(reader):
                if len(line) != 14:
                    raise BadFormatConfigAllowedFileTypesError()
                config_data.append(line)
        
        #For each file, read them and store their informations
        for filepath in filespath:
            tmp_data = self.readAFile(dict_data, filepath, config_data)

        """Return the triple hashmap containing the data of all the files"""
        return dict_data

    def readAFile(self, dict_data, filepath, config_data):
        """Read a 'hisea', 'paf' or 'mhap' file and store its data 
        in a triple hashmap (dictionnary in python)
        
        
        Attributes:
            filepath : the file's path
            dict_data : the triple hashmap
            config_data : config data describing the allowed file types
        """
        extension = filepath.split(".")[-1]
        extension_found = False

        for i in range(1, len(config_data)):
            #If the file's extension isn't mhap, hisea or paf, raise an error
            if config_data[i][0] == extension:
                extension_found = True
                dict_data = ExtractData().readAndExtract(filepath, dict_data, config_data[i])
        
        #If the extension isn't known, raise an error
        if not (extension_found):
            raise UnknownExtensionError(filepath + " : Unknown extension.")
        