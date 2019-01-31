import sys
from read.Parameters import Parameters
from read.ReadFiles import ReadFiles
from misc.AnalysisTools import *
from write.OutputWriter import *

from analysis_types.GentleTypeAnalysis import *
from analysis_types.CoverageTypeAnalysis import *
from analysis_types.StatisticsTypeAnalysis import *

class Analyzer:
    pass

def main(args):
    """Main function of the program"""
    
    parameters = Parameters()
    readFiles = ReadFiles()
    parser = parameters.complete_analyze(sys.argv[1:])
    parameters.additionnalAnalysis(parser)
    outputWriter = OutputWriter()

    dict_data = readFiles.readAllFiles(parser.files, "../allowed_files.csv")
    
    tools = AnalysisTools()

    for i_interval in tools.sort_Intervals_start(dict_data['1']['6696']['+'], True):
        print(i_interval.toStringInterval())

    print("=============================")
    
    if parser.analysis == "gentle":
        analysis = GentleTypeAnalysis()
        dict_data = analysis.analyse_data(dict_data)
    else:
        analysis = CoverageTypeAnalysis()
        if parser.analysis == "strict":
            dict_data = analysis.analyse_data(dict_data, parser.files, 0, None, parser.get_all)
        elif parser.analysis == "max":            
            dict_data = analysis.analyse_data(dict_data, parser.files, 1, None, parser.get_all)
        elif parser.analysis == "custom":
            if parser.moreThan is not None:
                dict_data = analysis.analyse_data(dict_data, parser.files, 11, int(parser.moreThan), parser.get_all)
            elif parser.lessThan is not None:
                dict_data = analysis.analyse_data(dict_data, parser.files, 12, int(parser.lessThan), parser.get_all)
            else:
                dict_data = analysis.analyse_data(dict_data, parser.files, 13, int(parser.equalsTo), parser.get_all)
            #analysis = CustomAnalysis()
            #dict_data = analysis.analyse_data(dict_data, parser.files, parser.moreThan, parser.lessThan, parser.equalsTo, parser.get_all)
        
    print("=============================")

    for i_interval in dict_data['1']['6696']['+']:
        print(i_interval.toStringInterval())

    # If the stat option is enabled, print some statistics about the files
    if parser.stats is True :
        statAnalyser = StatisticsTypeAnalysis()
        print(statAnalyser.statistics(dict_data, parser.files))

    if parser.no_output is False:
        if parser.output == "mhap":
            #outputWriter.outputMhap(dict_data)
            pass
        elif parser.output == "paf":
            #outputWriter.outputPaf(dict_data)
            pass
        else:
            print("Hisea output not implemented yet.")
            exit(0)
    else:
        print("No writing in an output file")
# Need this to run the main function
if __name__ == "__main__":
    main(sys.argv)
