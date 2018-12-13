import sys
from Parameters import Parameters
from ReadFiles import ReadFiles
from Iterator import *
from IteratorTools import *

class Analyzer:
    pass

def main(args):
    """Main function of the program"""
    
    parameters = Parameters()
    readFiles = ReadFiles()
    iterator = Iterator()
    parser = parameters.complete_analyze(sys.argv[1:])
    
    #dict = { 'Coucou': ['1', '2', '3', '4']}
    #print(dict['Coucou'][0])
    #readFiles.ReadAFile(parser.files[0])

    
    #readFiles.ExtractMhapData(parser.files[0])
    #readFiles.readAFile({}, parser.files[0])
    

    dict_data = readFiles.readAllFiles(parser.files, "../allowed_files.csv")
    #iterator.detect_overlaps(dict_data)
    

    tools = IteratorTools()

    for i_interval in tools.sort_Intervals_start(dict_data['1']['6696']['+'], True):
        print(i_interval.toStringInterval())
    print("=============================")
    
    dict_data = iterator.gentle_detection(dict_data)

    print("=============================")
    for i_interval in dict_data['1']['6696']['+']:
        print(i_interval.toStringInterval())


    # If the stat option is enabled, print some statistics about the files
    if parser.stats is True :
        print(iterator.statistics(dict_data, parser.files))

# Need this to run the main function
if __name__ == "__main__":
    main(sys.argv)
