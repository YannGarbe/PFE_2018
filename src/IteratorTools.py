import sys
from collections import defaultdict
from Parameters import Parameters
from ReadFiles import ReadFiles


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

        return intervals
    
    """
    def remove_duplicates(self, intervals):
        intervals_A = self.sort_Intervals_start(intervals, True)
        intervals_B = self.sort_Intervals_start(intervals, False)

        fo
    """