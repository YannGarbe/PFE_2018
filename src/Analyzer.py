import sys
from Parameters import Parameters
from ReadFiles import ReadFiles

class Analyzer:
    pass

def main(args):
    """Main function of the program"""
    
    parameters = Parameters()
    readFiles = ReadFiles()
    parser = parameters.complete_analyze(sys.argv[1:])
    
    #dict = { 'Coucou': ['1', '2', '3', '4']}
    #print(dict['Coucou'][0])
    #readFiles.ReadAFile(parser.files[0])

    
    #readFiles.ExtractMhapData(parser.files[0])
    readFiles.readAFile(parser.files[0])
    

    #dictData = readFiles.ReadAllFiles(parser.files)


# Need this to run the main function
if __name__ == "__main__":
    main(sys.argv)
