import unittest

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from read.Parameters import *
from misc.MyExceptions import *
from misc.Interval import *
from analysis_types.GentleTypeAnalysis import *

class test_analyse_gentle(unittest.TestCase):

    def test_gentle_no_fusion(self):
        dict_data = {}
        dict_data['1'] = {}
        dict_data['1']['2'] = {}
        dict_data['1']['2']['+'] = []

        inter1 = Interval("Test", 1, 2, "+", 50, 50, 15, 10, 75, 70)
        inter2 = Interval("Test", 1, 2, "+", 50, 50, 115, 110, 175, 170)
        inter3 = Interval("Test", 1, 2, "+", 50, 50, 215, 210, 275, 270)
        dict_data['1']['2']['+'].append(inter1)
        dict_data['1']['2']['+'].append(inter2)
        dict_data['1']['2']['+'].append(inter3)

        analysis = GentleTypeAnalysis()
        analysis.analyse_data(dict_data)

        self.assertEqual(3, len(dict_data['1']['2']['+']))
        self.assertEqual(inter1.toStringInterval(), dict_data['1']['2']['+'][0].toStringInterval())
        self.assertEqual(inter2.toStringInterval(), dict_data['1']['2']['+'][1].toStringInterval())
        self.assertEqual(inter3.toStringInterval(), dict_data['1']['2']['+'][2].toStringInterval())

    def test_gentle_one_fusion(self):
        dict_data = {}
        dict_data['1'] = {}
        dict_data['1']['2'] = {}
        dict_data['1']['2']['+'] = []

        inter1 = Interval("Test", 1, 2, "+", 50, 50, 15, 10, 75, 70)
        inter2 = Interval("Test", 1, 2, "+", 50, 50, 70, 65, 175, 170)
        inter3 = Interval("Test", 1, 2, "+", 50, 50, 215, 210, 275, 270)
        dict_data['1']['2']['+'].append(inter1)
        dict_data['1']['2']['+'].append(inter2)
        dict_data['1']['2']['+'].append(inter3)

        analysis = GentleTypeAnalysis()
        analysis.analyse_data(dict_data)

        result1 = Interval("Test", 1, 2, "+", 50, 50, 15, 10, 175, 170)
        self.assertEqual(2, len(dict_data['1']['2']['+']))
        self.assertEqual(inter3.toStringInterval(), dict_data['1']['2']['+'][0].toStringInterval())
        self.assertEqual(result1.toStringInterval(), dict_data['1']['2']['+'][1].toStringInterval())

    def test_gentle_full_fusion(self):
        dict_data = {}
        dict_data['1'] = {}
        dict_data['1']['2'] = {}
        dict_data['1']['2']['+'] = []

        inter1 = Interval("Test", 1, 2, "+", 50, 50, 15, 10, 75, 70)
        inter2 = Interval("Test", 1, 2, "+", 50, 50, 70, 65, 175, 170)
        inter3 = Interval("Test", 1, 2, "+", 50, 50, 115, 110, 275, 270)
        dict_data['1']['2']['+'].append(inter1)
        dict_data['1']['2']['+'].append(inter2)
        dict_data['1']['2']['+'].append(inter3)

        analysis = GentleTypeAnalysis()
        analysis.analyse_data(dict_data)

        result1 = Interval("Test", 1, 2, "+", 50, 50, 15, 10, 275, 270)
        self.assertEqual(1, len(dict_data['1']['2']['+']))
        self.assertEqual(result1.toStringInterval(), dict_data['1']['2']['+'][0].toStringInterval())