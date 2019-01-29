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

"""This class implements the gentle analysis, where the intervals are accepted once the max number of overlappers detect them"""
class MaxAnalysis:

    def analyse_data(self):
        pass