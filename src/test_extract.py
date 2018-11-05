import unittest
from MyExceptions import *
from Interval import Interval
from ExtractData import *

class Test_extract(unittest.TestCase):
    
    def test_extract_paf_one_line(self):
        extract_paf = ExtractDataPaf()
        