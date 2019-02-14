import unittest

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from misc.MyExceptions import *
from misc.Interval import Interval
from read.ReadFiles import *

class Test_read(unittest.TestCase):
    def test_read_config_file_type_not_found(self):
        readFiles = ReadFiles()
        with self.assertRaises(FileNotFoundError):
            readFiles.readAllFiles(["../../data/test.paf"], "non")

    def test_read_config_file_type_bad_format(self):
        readFiles = ReadFiles()
        with self.assertRaises(BadFormatConfigAllowedFileTypesError):
            readFiles.readAllFiles(["../data/test.paf"], "../../data/test.paf")

    def test_read_one_file_bad_unknown_extension(self):
        readFiles = ReadFiles()
        config_data = ['paf', '9', '16', '0', '5', '1', '6', '2', '7', '3', '8']
        with self.assertRaises(UnknownExtensionError):
            readFiles.readAFile({}, "../../data/test.mhap", config_data)

    def test_integration_with_paf_file_type(self):
        readFiles = ReadFiles()
        dict_test = readFiles.readAllFiles(["../../data/test.paf"], "../../allowed_files.csv")
        response = "test.paf: [id_A] : 1| [id_B] : 77893| [Strand] : -| [Length_A] : 1860| [Length_B] : 12237| [Start_A] : 1443| [Start_B] : 11803| [End_A] : 1810| [End_B] : 12172"
        #print(dict_test['77893']['1']['-'][0].toStringInterval())

        #self.assertEqual(response, dict_test['77893']['1']['-'][0].toStringInterval())
        self.assertEqual(response, dict_test['1']['77893']['-'][0].toStringInterval())

    