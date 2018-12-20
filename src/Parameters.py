import argparse
import os.path
from MyExceptions import *


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
        parser.add_argument("analysis", metavar="AnalysisType", default="gentle", choices=["gentle", "strict"],
                            help="The type of the analysis. 'gentle' allows all the possible informations. 'strict' allows the informations only if every overlappers are agree to ach other.")
        parser.add_argument('-s', '--stats', action='store_true')
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
