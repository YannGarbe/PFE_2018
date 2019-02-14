import unittest

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from read.Parameters import *
from misc.MyExceptions import *
from misc.Interval import *
from analysis_types.CoverageTypeAnalysis import *

class test_analyse_strict(unittest.TestCase):

    def test_strict_no_fusion_different_overlappers(self):
        dict_data = {}
        dict_data['1'] = {}
        dict_data['1']['2'] = {}
        dict_data['1']['2']['+'] = []

        inter1 = Interval("Test1", 1, 2, "+", 50, 50, 15, 10, 75, 70)
        inter2 = Interval("Test2", 1, 2, "+", 50, 50, 115, 110, 175, 170)
        inter3 = Interval("Test3", 1, 2, "+", 50, 50, 215, 210, 275, 270)
        dict_data['1']['2']['+'].append(inter1)
        dict_data['1']['2']['+'].append(inter2)
        dict_data['1']['2']['+'].append(inter3)

        analysis = CoverageTypeAnalysis()
        analysis.analyse_data(dict_data, ["Test1", "Test2", "Test3"], 0, None, False)

        self.assertEqual(0, len(dict_data['1']['2']['+']))

    def test_strict_no_fusion_same_overlappers(self):
        dict_data = {}
        dict_data['1'] = {}
        dict_data['1']['2'] = {}
        dict_data['1']['2']['+'] = []

        inter1 = Interval("Test1", 1, 2, "+", 50, 50, 15, 10, 75, 70)
        inter2 = Interval("Test1", 1, 2, "+", 50, 50, 115, 110, 175, 170)
        inter3 = Interval("Test1", 1, 2, "+", 50, 50, 215, 210, 275, 270)
        dict_data['1']['2']['+'].append(inter1)
        dict_data['1']['2']['+'].append(inter2)
        dict_data['1']['2']['+'].append(inter3)

        analysis = CoverageTypeAnalysis()
        analysis.analyse_data(dict_data, ["Test1", "Test2", "Test3"], 0, None, False)

        self.assertEqual(0, len(dict_data['1']['2']['+']))

    def test_strict_no_fusion_different_overlappers_2_good_overlappers(self):
        dict_data = {}
        dict_data['1'] = {}
        dict_data['1']['2'] = {}
        dict_data['1']['2']['+'] = []

        inter1 = Interval("Test1", 1, 2, "+", 50, 50, 15, 10, 175, 170)
        inter2 = Interval("Test2", 1, 2, "+", 50, 50, 115, 110, 175, 170)
        inter3 = Interval("Test3", 1, 2, "+", 50, 50, 215, 210, 275, 270)
        dict_data['1']['2']['+'].append(inter1)
        dict_data['1']['2']['+'].append(inter2)
        dict_data['1']['2']['+'].append(inter3)

        analysis = CoverageTypeAnalysis()
        analysis.analyse_data(dict_data, ["Test1", "Test2", "Test3"], 0, None, False)

        self.assertEqual(0, len(dict_data['1']['2']['+']))

    def test_strict_fusion_different_overlappers(self):
        dict_data = {}
        dict_data['1'] = {}
        dict_data['1']['2'] = {}
        dict_data['1']['2']['+'] = []

        inter1 = Interval("Test1", 1, 2, "+", 50, 50, 15, 10, 175, 170)
        inter2 = Interval("Test2", 1, 2, "+", 50, 50, 115, 110, 215, 225)
        inter3 = Interval("Test3", 1, 2, "+", 50, 50, 150, 160, 275, 270)
        dict_data['1']['2']['+'].append(inter1)
        dict_data['1']['2']['+'].append(inter2)
        dict_data['1']['2']['+'].append(inter3)

        analysis = CoverageTypeAnalysis()
        analysis.analyse_data(dict_data, ["Test1", "Test2", "Test3"], 0, None, False)
        
        result1 = Interval("Test1", 1, 2, "+", 50, 50, 150, 160, 175, 170)
        self.assertEqual(1, len(dict_data['1']['2']['+']))
        self.assertEqual(result1.toStringInterval(), dict_data['1']['2']['+'][0].toStringInterval())
