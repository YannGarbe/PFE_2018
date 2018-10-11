import argparse
import os.path
from MyExceptions import *


class Parameters:
    def complete_analyze(self, args):
        """Verify the arguments of the program
        Step 1 : Parse the arguments
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
        parser.add_argument("output", metavar="Output_Type", default="mhap", choices=["hisea", "mhap", "paf"],
                            help="The extension of the created output file. It can be either 'hisea', 'mhap' or 'paf'")
        parser.add_argument("files", metavar="Input_Result_Files", nargs="+",
                            help="The files of the overlappers's results")

        """Returns the parsed Args"""
        return parser.parse_args(args)

    def check_files(self, filespath):
        """Verify the files' location and extension

        Attributes
            files: An Array containing the file's names
        """
        for file in filespath:
            if not(file.endswith('mhap') or file.endswith('hisea') or file.endswith('paf')):
                raise BadExtensionError(file + " : Bad extension. Must be '.mhap', '.pad' or '.hisea'")
        
            if not(os.path.isfile(file)):
                raise FileNotFoundError(file + " : Not Found")
        """Return the files' array"""
        return filespath