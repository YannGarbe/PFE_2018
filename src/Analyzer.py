import sys
from read.Parameters import Parameters
from read.ReadFiles import ReadFiles
from analysis_types.Iterator import *
from misc.IteratorTools import *
from write.OutputWriter import *

class Analyzer:
    pass

def main(args):
    """Main function of the program"""
    
    parameters = Parameters()
    readFiles = ReadFiles()
    iterator = Iterator()
    parser = parameters.complete_analyze(sys.argv[1:])
    outputWriter = OutputWriter()
    
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
    
    if parser.analysis == "gentle":
        dict_data = iterator.gentle_detection(dict_data)
    elif parser.analysis == "strict":
        dict_data = iterator.strict_detection(dict_data, parser.files)
    elif parser.analysis == "max":
        dict_data = iterator.strict_detection(dict_data, parser.files)
        
    print("=============================")

    for i_interval in dict_data['1']['6696']['+']:
        print(i_interval.toStringInterval())

    # If the stat option is enabled, print some statistics about the files
    if parser.stats is True :
        print(iterator.statistics(dict_data, parser.files))

    if parser.output == "mhap":
        #outputWriter.outputMhap(dict_data)
        pass
    elif parser.output == "paf":
        #outputWriter.outputPaf(dict_data)
        pass
    else:
        print("Hisea output not implemented yet.")
        exit(0)

# Need this to run the main function
if __name__ == "__main__":
    main(sys.argv)
