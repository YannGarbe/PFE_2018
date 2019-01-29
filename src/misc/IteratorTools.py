import sys
from collections import defaultdict

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from read.Parameters import Parameters
from read.ReadFiles import ReadFiles

class IteratorTools:
    def sort_Intervals_start(self, intervals, startA):
        """Sort the interval list by the start index
        
        Attributes:
            intervals : the interval list
            read_number : true to sort by the readA start index, false to sort by the readB start Index
        """

        for i in range(0, len(intervals)):
            tmp_interval = None
            min_interval = None
            min_j = 0
        
            #Find the interval who has the smallest index of begin
            for j in range(i, len(intervals)):
                if min_interval is None:
                    min_interval = intervals[j]
                    min_j = j
                
                if startA:
                    if intervals[j].start_A < min_interval.start_A :
                        min_interval = intervals[j]
                        min_j = j
                else:
                    if intervals[j].start_B < min_interval.start_B :
                        min_interval = intervals[j]
                        min_j = j

            tmp_interval = intervals[i]
            intervals[i] = intervals[min_j]
            intervals[min_j] = tmp_interval
        """Returns the sorted intervals"""
        return intervals

    def retrieve_id_strict_analysis(self, filespath, max_interval_N, cover_N, list_id_N):
        for i in range(len(cover_N)):


            if len(cover_N[i]) == max_interval_N:
                for curr_filepath in filespath:
                    curr_filename = curr_filepath.split("/")[-1]

                    contains_the_curr_overlapper = False
                    for curr_interval in cover_N[i]:
                        if curr_interval.getFilename() == curr_filename:
                            #The curr_overlapper has detected an interval
                            contains_the_curr_overlapper = True
                            break
                    #The curr_overlapper hasn't detected an interval. It's time to move on
                    if not contains_the_curr_overlapper:
                        break
                list_id_N.append(i)
        return list_id_N