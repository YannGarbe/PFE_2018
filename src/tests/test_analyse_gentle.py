import unittest

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from misc.MyExceptions import *
from misc.Interval import Interval
from read.ExtractData import *

class test_analyse_gentle(unittest.TestCase):

    def test