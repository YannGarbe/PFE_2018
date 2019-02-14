import unittest

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from misc.MyExceptions import *
from misc.Interval import Interval
from read.ExtractData import *

class Test_extract(unittest.TestCase):

    def test_extract_not_enough_fields_data_file(self):
        config_file_type = ['paf', '9', '17', '0', '5', '1', '6', '2', '7', '3', '8', '1']
        extract = ExtractData()

        with self.assertRaises(BadFormatFileError):
            extract.readAndExtract("../../data/test.paf", {}, config_file_type)

    def test_extract_interval_creation(self):
        config_file_type = ['paf', '9', '12', '0', '5', '1', '6', '2', '7', '3', '8', '1', '4', 'N']
        extract = ExtractData()

        dict_test = extract.readAndExtract("../../data/test.paf", {}, config_file_type)
        response = "test.paf: [id_A] : 1| [id_B] : 77893| [Strand] : -| [Length_A] : 1860| [Length_B] : 12237| [Start_A] : 1443| [Start_B] : 11803| [End_A] : 1810| [End_B] : 12172"

        #self.assertEqual(response, dict_test['77893']['1']['-'][0].toStringInterval())
        self.assertEqual(response, dict_test['1']['77893']['-'][0].toStringInterval())

    