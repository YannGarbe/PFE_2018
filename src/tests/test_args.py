import unittest
from Parameters import Parameters
from MyExceptions import *

class Test_args(unittest.TestCase):

    #================================================
    #==============Parser Section====================
    #================================================

    def test_parser_no_parameters_incorrect(self):
        parameters = Parameters()
        with self.assertRaises(SystemExit):
            parameters.parse_args([])
    
    def test_parser_one_file_correct(self):
        parameters = Parameters()
        parser = parameters.parse_args(['mhap','heyo'])
        self.assertEqual('mhap', parser.output)
        self.assertEqual(['heyo'], parser.files)

    def test_parser_several_files_correct(self):
        parameters = Parameters()
        parser = parameters.parse_args(['hisea','heyo', 'we', 'are', 'files'])
        self.assertEqual('hisea', parser.output)
        self.assertEqual(['heyo', 'we', 'are', 'files'], parser.files)

    def test_parser_several_files_incorrect_output(self):
        parameters = Parameters()
        with self.assertRaises(SystemExit):
            parameters.parse_args(['Bad','heyo', 'we', 'are', 'files'])

    #================================================
    #==============File Section======================
    #================================================


    def test_check_files_files_correct(self):
        parameters = Parameters()
        files = ['../data/test.mhap', '../data/test.hisea', '../data/test.paf']
        res = parameters.check_files(files)
        self.assertEqual(files, res)
    """
    def test_check_files_files_bad_extension(self):
        parameters = Parameters()
        files = ['../data/test.mhap', '../data/test.hisea', 'idea.txt']
        with self.assertRaises(BadExtensionError):
            parameters.check_files(files)
    """
    
    def test_check_files_files_bad_extension(self):
        parameters = Parameters()
        files = ['../data/test.mhap', '../data/test.hisea', 'idea.paf']
        with self.assertRaises(FileNotFoundError):
            parameters.check_files(files)