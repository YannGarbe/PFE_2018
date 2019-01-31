import sys
import math
from collections import defaultdict

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from read.Parameters import Parameters
from read.ReadFiles import ReadFiles
from misc.AnalysisTools import *
from misc.Interval import *

"""This class implements the statistic analysis of the data"""
class StatisticsTypeAnalysis:

    def statistics(self, dict_data, filespath):
        """Iterates through the triple hashmap of itervals to make some statistics.
        
        Attributes:
            dict_data : the triple hashmap containing the itervals of the overlappers
            nb_input_files : the number of the input files 
        """
        nb_intervals = 0
        nb_connections = 0

        tmp_total = 0.00

        known_types = []

        avg_total_list = []
        avg_total = 0.00

        # avg_coherent_list = []
        # avg_coherent = 0.00
        dict_total = {}
        # dict_total = defaultdict(list)
        list_dict_total = []
        
        # dict_duplicate = defaultdict(list)
        dict_duplicate = {}
        
        for id_a in dict_data:
            for id_b in dict_data[id_a]:
                for strand in dict_data[id_a][id_b]:
                    list_duplicate = []
                    dict_total = {}

                    intervals = dict_data[id_a][id_b][strand]

                    # Count the number of "connections" between two read 2
                    nb_connections += 1

                    # Process the avg intervals per overlap
                    avg_total_list.append(float(len(intervals)))

                    # Iterate through found intervals
                    for i_interval in intervals :

                        i_extension = i_interval.getFilename().split(".")[-1]

                        # Count the number of intervals
                        nb_intervals += 1

                        # Analyse if the extension is known
                        if i_extension not in known_types:
                            known_types.append(i_extension)
                        
                        # Check if 
                        if i_interval.getFilename() not in dict_total:
                            dict_total[i_interval.getFilename()] = 1.00
                        else:
                            dict_total[i_interval.getFilename()] += 1.00
                        
                    list_dict_total.append(dict_total)
                
        file_type_str = ""
        for fileType in known_types :
            file_type_str += fileType + " | "

        # Create the first part of the report (general part)

        if (len(filespath) == 1):
            dep_percent = math.floor( (((sum(avg_total_list)/len(avg_total_list) ) / len(filespath))-1 )* 100) 
        else:
            dep_percent = math.floor( (((sum(avg_total_list)/len(avg_total_list)) -1) / (len(filespath)-1) )* 100) 
        report = ("Report of the program data >>>\n"
        "\tNumber of times there is at least one interval between two reads = " + str(nb_connections) + "\n"
        "\tTotal intervals = " + str(nb_intervals) + "\n"
        "\tKnown file types = " + file_type_str + "\n\n"
        
        "\tAvg of intervals per overlap = " + str(sum(avg_total_list)/len(avg_total_list)) + "\n"
        "\tDependance of percentage of the analysis = " + str(dep_percent)  + "%\n"
        "=========================================================\n"
        "Per file >>>\n"
        )

        # Create the second part of the report (specific part)
        for filepath in filespath :
            filename = filepath.split("/")[-1]
            i_list = []

            for i_dict in list_dict_total:
                if filename in i_dict:
                    i_list.append(float(i_dict[filename]))            
            report += (
            "" + filename + "\n"
            "\tTotal intervals number in this file = " + str(sum(i_list)) + "\n"
            "\tAvg of intervals repetitions in this file = " + str(sum(i_list)/len(i_list)) + "\n"
            )

        """Returns the generated report"""
        return report                                           