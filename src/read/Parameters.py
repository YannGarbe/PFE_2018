import argparse
import os.path

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from misc.MyExceptions import *


class Parameters:
    def complete_analyze(self, args):
        """Verify the arguments of the program
        Step 1: Parse the arguments
        Step 2: Verify the files' location and extension

        Attributes
            args: An array containing the arguments
        """

        params = self.parse_args(args)
        self.check_files(params.files)

        return params

    def parse_args(self, args):
        """Define an argument parser for the program

        Attributes:
            args: An array containing the arguments
        """
        parser = argparse.ArgumentParser(
            description="Analyze Overlappers' results.")
        parser.add_argument("analysis", metavar="AnalysisType", default="gentle", choices=["gentle", "strict", "max", "custom"],
                            help="The type of the analysis. 'gentle' allows all the possible informations. " +
                            "'strict' allows the informations only if every overlappers are agree with each other." +
                            "'max' allows the informations only if a maximum of overlappers are agree with each other." + 
                            "'custom' allows the informations only if N overlappers are agree with each other." +
                            "'strict' allows the informations only if every overlappers are agree with each other.")
        #parser.add_argument('custom_number', metavar="CustomType", default="1" help="N number of overlapppers for the custom option")
        parser.add_argument('-s', '--stats', action='store_true', help="Display statistics about the input files")        
        parser.add_argument("output", metavar="OutputType", default="mhap", choices=["hisea", "mhap", "paf"],
                            help="The extension of the created output file. It can be either 'hisea', 'mhap' or 'paf'")
        parser.add_argument("files", metavar="InputFiles", nargs="+",
                            help="The files of the overlappers's results")

        """Returns the parsed Args"""
        return parser.parse_args(args)

    def check_files(self, filespath):
        """Verify the files' location and extension

        Attributes
            files: An Array containing the file's names
        """

        # For each file's path in the file path array
        for file in filespath:
            # If the file's path is wrong, or the file doesn't exist, raise an error
            if not(os.path.isfile(file)):
                raise FileNotFoundError(file + " : Not Found")
        """Return the files' array"""
        return filespath
