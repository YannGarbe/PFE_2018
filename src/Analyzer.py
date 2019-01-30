import sys
from read.Parameters import Parameters
from read.ReadFiles import ReadFiles
from misc.AnalysisTools import *
from write.OutputWriter import *

from analysis_types.CustomAnalysis import *
from analysis_types.GentleAnalysis import *
from analysis_types.MaxAnalysis import *
from analysis_types.StrictAnalysis import *
from analysis_types.StatisticsAnalysis import *

class Analyzer:
    pass

def main(args):
    """Main function of the program"""
    
    parameters = Parameters()
    readFiles = ReadFiles()
    parser = parameters.complete_analyze(sys.argv[1:])
    parameters.additionnalAnalysis(parser)
    outputWriter = OutputWriter()
    
    
    #dict = { 'Coucou': ['1', '2', '3', '4']}
    #print(dict['Coucou'][0])
    #readFiles.ReadAFile(parser.files[0])

    
    #readFiles.ExtractMhapData(parser.files[0])
    #readFiles.readAFile({}, parser.files[0])
    

    dict_data = readFiles.readAllFiles(parser.files, "../allowed_files.csv")
    #iterator.detect_overlaps(dict_data)
    

    tools = AnalysisTools()

    for i_interval in tools.sort_Intervals_start(dict_data['1']['6696']['+'], True):
        print(i_interval.toStringInterval())

    print("=============================")
    
    if parser.analysis == "gentle":
        analysis = GentleAnalysis()
        dict_data = analysis.analyse_data(dict_data)

    elif parser.analysis == "strict":
        analysis = StrictAnalysis()
        dict_data = analysis.analyse_data(dict_data, parser.files, parser.get_all)
    elif parser.analysis == "max":
        analysis = MaxAnalysis()
        dict_data = analysis.analyse_data(dict_data, parser.files, parser.get_all)
        
    elif parser.analysis == "custom":
        analysis = CustomAnalysis()
        dict_data = analysis.analyse_data(dict_data, parser.files, parser.moreThan, parser.lessThan, parser.equalsTo, parser.get_all)
    
    print("=============================")

    for i_interval in dict_data['1']['6696']['+']:
        print(i_interval.toStringInterval())

    # If the stat option is enabled, print some statistics about the files
    if parser.stats is True :
        statAnalyser = StatisticsAnalysis()
        print(statAnalyser.statistics(dict_data, parser.files))

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
