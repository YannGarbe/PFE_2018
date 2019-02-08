import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from read.Parameters import Parameters
from read.ReadFiles import ReadFiles
from misc.AnalysisTools import *
from misc.Interval import *

"""This class implements the gentle analysis, where all the intervals are accepted"""
class GentleTypeAnalysis:

    def analyse_data(self, dict_data):
        tools = AnalysisTools()
        for id_a in dict_data:
            for id_b in dict_data[id_a]:
                for strand in dict_data[id_a][id_b]:
                    intervals = dict_data[id_a][id_b][strand]
                    if len(intervals) > 1:
                        intervals = tools.sort_Intervals_start(intervals, True)

                        i_max_run = len(intervals)

                        #Loop to be sure to catch all the possibilities
                        # (In case a interval is not compatible at T0, 
                        #   but is at T1 because the curr_interval would be not the same)
                        for _ in range(0, i_max_run):
                        
                            interval_max = intervals[0]
                            #Retrieves the first element of the list and moves it away
                            curr_list_intervals = []
                            del intervals[0]

                            #Loop until the list is empty
                            while len(intervals) > 0:
                                tmp_interval = intervals[0]
                                del intervals[0]
                                if interval_max.compareAndFusion_gentle(tmp_interval) == 0:
                                    curr_list_intervals.append(tmp_interval)
                            curr_list_intervals.append(interval_max)
                            
                            dict_data[id_a][id_b][strand] = curr_list_intervals
                            intervals = dict_data[id_a][id_b][strand]

        return dict_data              
