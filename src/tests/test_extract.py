import unittest
from MyExceptions import *
from Interval import Interval
from ExtractData import *

class Test_extract(unittest.TestCase):
    def test_extract_too_many_fields_data_file(self):
        config_file_type = ['paf', '9', '17', '0', '5', '1', '6', '2', '7', '3', '8']
        extract = ExtractData()

        with self.assertRaises(BadFormatFileError):
            extract.readAndExtract("../data/test.paf", {}, config_file_type)

    def test_extract_interval_creation(self):
        config_file_type = ['paf', '9', '16', '0', '5', '1', '6', '2', '7', '3', '8']
        extract = ExtractData()

        dict_test = extract.readAndExtract("../data/test.paf", {}, config_file_type)
        response = "test.paf: [id_A] > 2| [id_B] > 77893| [Length_A] > 10636| [Length_B] > 12237| [Start_A] > 78| [Start_B] > 8505| [End_A] > 3562| [End_B] > 12181"

        self.assertEqual(response, dict_test['77893']['2'][0].toStringInterval())
        self.assertEqual(response, dict_test['2']['77893'][0].toStringInterval())

    