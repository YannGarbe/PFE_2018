import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from misc.AnalysisTools import *
from misc.Interval import *

def warning_max_interval_greater_than_length_overlappers(list_interval, list_filepaths):
    print("Warning : There are more intervals than overlappers (the duplicates have been removed)")
    print("The intervals")
    for interval in list_interval:
        print("\t",interval.toStringInterval())
    print("The files")
    for filepath in list_filepaths:
        print("\t",filepath)

def warning_max_interval_A_is_not_equal_to_max_interval_B(list_interval_A, list_interval_B):
    pass