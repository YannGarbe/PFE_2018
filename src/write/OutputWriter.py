from misc.AnalysisTools import *
import datetime

import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


"""This class writes the data dictionnary in a specific file (depending on the file type."""
class OutputWriter:

    def __init__(self, analysis_type):
        self.analysis_type = analysis_type
        self.curr_year = str(datetime.datetime.now().year)

        if datetime.datetime.now().month < 10:
            self.curr_month ="0" + str(datetime.datetime.now().month)
        else:    
            self.curr_month = str(datetime.datetime.now().month)

        if datetime.datetime.now().day < 10:
            self.curr_day = "0" + str(datetime.datetime.now().day)
        else:
            self.curr_day = str(datetime.datetime.now().day)

        if datetime.datetime.now().hour < 10:
            self.curr_hour = "0" + str(datetime.datetime.now().hour)
        else:
            self.curr_hour = str(datetime.datetime.now().hour)
    
        if datetime.datetime.now().minute < 10:
            self.curr_minute = "0" + str(datetime.datetime.now().minute)
        else:
            self.curr_minute = str(datetime.datetime.now().minute)
        
        if datetime.datetime.now().second < 10:
            self.curr_second = "0" + str(datetime.datetime.now().second)
        else:
            self.curr_second = str(datetime.datetime.now().second)

        self.curr_complete_date = self.curr_year + self.curr_month + self.curr_day + "-" + self.curr_hour + self.curr_minute +self.curr_second 

    def outputMhap(self, dict_data):
        """Write the data dictionnary (triple hashmap of intervals) in a mhap file
        The file follows the mhap data structure

        Attributes
            dict_data: the data dictionnary
        """
        tools = AnalysisTools()
        file = open("../Output/Mhap-" + self.analysis_type + "-" +self.curr_complete_date + ".mhap", "w")
        for id_a in dict_data:
            for id_b in dict_data[id_a]:
                for strand in dict_data[id_a][id_b]:
                    intervals=dict_data[id_a][id_b][strand]
                    intervals=tools.sort_Intervals_start(intervals, True)
                    for i_interval in intervals:
                        strand_A=0
                        strand_B=0
                        if i_interval.getStrand() == '-':
                            strand_A=0
                            strand_B=1

                        interval_line=(str(i_interval.getId_A()) + " "
                        "" + str(i_interval.getId_B()) + " "
                        "" + "0.0" + " "
                        "" + "0" + " "
                        "" + str(strand_A) + " "
                        "" + str(i_interval.getStart_A()) + " "
                        "" + str(i_interval.getEnd_A()) + " "
                        "" + str(i_interval.getLength_A()) + " "
                        "" + str(strand_B) + " "
                        "" + str(i_interval.getStart_B()) + " "
                        "" + str(i_interval.getEnd_B()) + " "
                        "" + str(i_interval.getLength_B()) + "\n")

                        file.write(interval_line)
        file.close()


    def outputPaf(self, dict_data):
        """Write the data dictionnary (triple hashmap of intervals) in a paf file
        The file follows the paf data structure

        Attributes
            dict_data: the data dictionnary
        """
        tools=AnalysisTools()
        file=open("../Output/Paf-" + self.analysis_type + "-" + self.curr_complete_date + ".paf", "w")
        for id_a in dict_data:
            for id_b in dict_data[id_a]:
                for strand in dict_data[id_a][id_b]:
                    intervals=dict_data[id_a][id_b][strand]
                    intervals=tools.sort_Intervals_start(intervals, True)
                    for i_interval in intervals:

                        interval_line=(str(i_interval.getId_A()) + "\t"
                        "" + str(i_interval.getLength_A()) + "\t"
                        "" + str(i_interval.getStart_A()) + "\t"
                        "" + str(i_interval.getEnd_A()) + "\t"
                        "" + str(i_interval.getStrand()) + "\t"
                        "" + str(i_interval.getId_B()) + "\t"
                        "" + str(i_interval.getLength_B()) + "\t"
                        "" + str(i_interval.getStart_B()) + "\t"
                        "" + str(i_interval.getEnd_B()) + "\t"
                        "" + "0" + "\t"
                        "" + "0" + "\t"
                        "" + "0" + "\t"
                        "" + "/" + "\t"
                        "" + "/" + "\t"
                        "" + "/" + "\t"
                        "" + "/" + "\n")
                        file.write(interval_line)
        file.close()
