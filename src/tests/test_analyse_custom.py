import unittest

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from read.Parameters import *
from misc.MyExceptions import *
from misc.Interval import *
from analysis_types.CoverageTypeAnalysis import *

class test_analyse_max(unittest.TestCase):

    def test_custom_more_than_no_accept(self):
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
        analysis.analyse_data(dict_data, ["Test1", "Test2", "Test3"], 11, 2, False)

        self.assertEqual(0, len(dict_data['1']['2']['+']))

    def test_custom_more_than_accept(self):
        dict_data = {}
        dict_data['1'] = {}
        dict_data['1']['2'] = {}
        dict_data['1']['2']['+'] = []

        inter1 = Interval("Test1", 1, 2, "+", 50, 50, 15, 10, 175, 170)
        inter2 = Interval("Test2", 1, 2, "+", 50, 50, 115, 110, 150, 160)
        inter3 = Interval("Test3", 1, 2, "+", 50, 50, 100, 100, 275, 270)
        dict_data['1']['2']['+'].append(inter1)
        dict_data['1']['2']['+'].append(inter2)
        dict_data['1']['2']['+'].append(inter3)

        analysis = CoverageTypeAnalysis()
        analysis.analyse_data(dict_data, ["Test1", "Test2", "Test3"], 11, 2, False)

        self.assertEqual(1, len(dict_data['1']['2']['+']))
        
        result1 = Interval("Test1", 1, 2, "+", 50, 50, 115, 110, 150, 160)
        self.assertEqual(result1.toStringInterval(), dict_data['1']['2']['+'][0].toStringInterval())


    def test_custom_less_than_no_accept(self):
        dict_data = {}
        dict_data['1'] = {}
        dict_data['1']['2'] = {}
        dict_data['1']['2']['+'] = []

        inter1 = Interval("Test1", 1, 2, "+", 50, 50, 115, 110, 175, 170)
        inter2 = Interval("Test2", 1, 2, "+", 50, 50, 115, 110, 175, 170)
        inter3 = Interval("Test3", 1, 2, "+", 50, 50, 115, 110, 175, 170)
        dict_data['1']['2']['+'].append(inter1)
        dict_data['1']['2']['+'].append(inter2)
        dict_data['1']['2']['+'].append(inter3)

        analysis = CoverageTypeAnalysis()
        analysis.analyse_data(dict_data, ["Test1", "Test2", "Test3"], 12, 2, False)

        self.assertEqual(0, len(dict_data['1']['2']['+']))
        
    def test_custom_less_than_accept(self):
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
        analysis.analyse_data(dict_data, ["Test1", "Test2", "Test3"], 12, 2, False)

        self.assertEqual(1, len(dict_data['1']['2']['+']))
        
        result1 = Interval("Test1", 1, 2, "+", 50, 50, 215, 210, 275, 270)
        self.assertEqual(result1.toStringInterval(), dict_data['1']['2']['+'][0].toStringInterval())

    def test_custom_equals_to_no_accept(self):
        dict_data = {}
        dict_data['1'] = {}
        dict_data['1']['2'] = {}
        dict_data['1']['2']['+'] = []

        inter1 = Interval("Test1", 1, 2, "+", 50, 50, 115, 110, 175, 170)
        inter2 = Interval("Test2", 1, 2, "+", 50, 50, 115, 110, 175, 170)
        inter3 = Interval("Test3", 1, 2, "+", 50, 50, 115, 110, 175, 170)
        dict_data['1']['2']['+'].append(inter1)
        dict_data['1']['2']['+'].append(inter2)
        dict_data['1']['2']['+'].append(inter3)

        analysis = CoverageTypeAnalysis()
        analysis.analyse_data(dict_data, ["Test1", "Test2", "Test3"], 12, 2, False)

        self.assertEqual(0, len(dict_data['1']['2']['+']))
        

    def test_custom_equals_to_accept(self):
        dict_data = {}
        dict_data['1'] = {}
        dict_data['1']['2'] = {}
        dict_data['1']['2']['+'] = []

        inter1 = Interval("Test1", 1, 2, "+", 50, 50, 15, 10, 175, 170)
        inter2 = Interval("Test2", 1, 2, "+", 50, 50, 115, 110, 150, 160)
        inter3 = Interval("Test3", 1, 2, "+", 50, 50, 215, 210, 275, 270)
        dict_data['1']['2']['+'].append(inter1)
        dict_data['1']['2']['+'].append(inter2)
        dict_data['1']['2']['+'].append(inter3)

        analysis = CoverageTypeAnalysis()
        analysis.analyse_data(dict_data, ["Test1", "Test2", "Test3"], 13, 2, False)

        self.assertEqual(1, len(dict_data['1']['2']['+']))
        
        result1 = Interval("Test1", 1, 2, "+", 50, 50, 115, 110, 150, 160)
        self.assertEqual(result1.toStringInterval(), dict_data['1']['2']['+'][0].toStringInterval())