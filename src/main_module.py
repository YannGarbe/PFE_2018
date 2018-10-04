import sys
import argparse

def parse_args(args):
    """Define an argument parser for the program
    
    Attributes:
        args: A string containing the arguments
    """
    parser = argparse.ArgumentParser(description="Analyze Overlappers' results.")
    parser.add_argument("output", metavar="Output_Type", default="mhap", choices=["hisea", "mhap", "paf"],
        help="The extension of the created output file. It can be either 'hisea', 'mhap' or 'paf'")
    parser.add_argument("files", metavar="Input_Result_Files", nargs="+",
        help="The files of the overlappers's results")

    return parser.parse_args(args)

def main(args):
    """Main function of the program"""
    parser = parse_args(sys.argv[1:])
    print(parser._get_args)
    
    

#Need this to run the main function
if __name__ == "__main__":
    main(sys.argv)