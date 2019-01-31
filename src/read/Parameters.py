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
        parser.add_argument('-m', '--moreThan', action='store', help="Custom parameter. allows the informations only if more than N overlappers are agree with each other.")
        parser.add_argument('-l', '--lessThan', action='store', help="Custom parameter. allows the informations only if less than N overlappers are agree with each other.")
        parser.add_argument('-e', '--equalsTo', action='store', help="Custom parameter. allows the informations only if exactly N overlappers are agree with each other.")
        parser.add_argument('-s', '--stats', action='store_true', help="Display statistics about the input files")
        parser.add_argument('-all', '--get_all', action='store_true', help="Get all the intervals in a custom, max, or strict analysis")
        parser.add_argument('-n', '--no_output', action='store_true', help="Don't export the analysis in a file")
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

    def additionnalAnalysis(self, parser):
        if parser.analysis == "custom" and parser.moreThan is None and parser.lessThan is None and parser.equalsTo is None:
            raise ParameterError("custom analysis is asked without a 'moreThan' (-m), a 'lessThan' (-l) or a 'equalsTo' (-e)")
        
        if parser.moreThan is not None:
            if parser.lessThan is not None or parser.equalsTo is not None:
                raise ParameterError("custom analysis is asked with 2 options or more. Only one is needed")
            if int(parser.moreThan) < 0:
                raise ParameterError("custom analysis is asked with the 'moreThan' option but the value is negative")
        
        if parser.lessThan is not None:
            if parser.moreThan is not None or parser.equalsTo is not None:
                raise ParameterError("custom analysis is asked with 2 options or more. Only one is needed")
            if int(parser.lessThan) < 1:
                raise ParameterError("custom analysis is asked with the 'lessThan' option but the value is less than 1")

        if parser.equalsTo is not None:
            if parser.lessThan is not None or parser.moreThan is not None:
                raise ParameterError("custom analysis is asked with 2 options or more. Only one is needed")
            if int(parser.equalsTo) < 1:
                raise ParameterError("custom analysis is asked with the 'equalsTo' option but the value is less than 1")