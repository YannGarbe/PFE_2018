import unittest
from MyExceptions import *
from Interval import Interval
from ReadFiles import *

class Test_read(unittest.TestCase):
    def test_read_config_file_type_not_found(self):
        readFiles = ReadFiles()
        with self.assertRaises(FileNotFoundError):
            readFiles.readAllFiles(["../data/test.paf"], "non")

    def test_read_config_file_type_bad_format(self):
        readFiles = ReadFiles()
        with self.assertRaises(BadFormatConfigAllowedFileTypesError):
            readFiles.readAllFiles(["../data/test.paf"], "../data/test.paf")

    def test_read_one_file_bad_unknown_extension(self):
        readFiles = ReadFiles()
        config_data = ['paf', '9', '16', '0', '5', '1', '6', '2', '7', '3', '8']
        with self.assertRaises(UnknownExtensionError):
            readFiles.readAFile({}, "../data/test.mhap", config_data)

    def test_integration_with_paf_file_type(self):
        readFiles = ReadFiles()
        dict_test = readFiles.readAllFiles(["../data/test.paf"], "../allowed_files.csv")
        response = "test.paf: [id_A] > 2| [id_B] > 77893| [Length_A] > 10636| [Length_B] > 12237| [Start_A] > 78| [Start_B] > 8505| [End_A] > 3562| [End_B] > 12181"

        self.assertEqual(response, dict_test['77893']['2'][0].toStringInterval())
        self.assertEqual(response, dict_test['2']['77893'][0].toStringInterval())

    