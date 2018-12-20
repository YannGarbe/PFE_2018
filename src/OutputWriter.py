import datetime
from IteratorTools import *

class OutputWriter:

    def outputMhap(self, dict_data):
        tools = IteratorTools()
        file = open("../Output/Mhap-" + str(datetime.datetime.now().time()) + ".txt", "w")
        for id_a in dict_data:
            for id_b in dict_data[id_a]:
                for strand in dict_data[id_a][id_b]:
                    intervals = dict_data[id_a][id_b][strand]
                    intervals = tools.sort_Intervals_start(intervals, True)
                    for i_interval in intervals:
                        
                        strand_A = 0
                        strand_B = 0
                        if i_interval.getStrand() == '-':
                            strand_A = 0
                            strand_B = 1
                        
                        interval_line = (str(i_interval.getId_A()) + " "
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
                        print(interval_line)
                        file.write(interval_line)
        file.close()


    def outputPaf(self, dict_data):
        tools = IteratorTools()
        file = open("../Output/Paf-" + str(datetime.datetime.now().time()) + ".txt", "w")
        for id_a in dict_data:
            for id_b in dict_data[id_a]:
                for strand in dict_data[id_a][id_b]:
                    intervals = dict_data[id_a][id_b][strand]
                    intervals = tools.sort_Intervals_start(intervals, True)
                    for i_interval in intervals:
                        
                        interval_line = (str(i_interval.getId_A()) + "\t"
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
                        print(interval_line)
                        file.write(interval_line)
        file.close()