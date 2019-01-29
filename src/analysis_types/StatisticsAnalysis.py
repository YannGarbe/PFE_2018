import sys
import math
from collections import defaultdict

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from read.Parameters import Parameters
from read.ReadFiles import ReadFiles
from misc.AnalysisTools import *
from misc.Interval import *

class StatisticsAnalysis:
    
    def gentle_detection(self, dict_data):
        tools = AnalysisTools()
        for id_a in dict_data:
            for id_b in dict_data[id_a]:
                for strand in dict_data[id_a][id_b]:
                    intervals = dict_data[id_a][id_b][strand]
                    if len(intervals) > 1:
                        intervals = tools.sort_Intervals_start(intervals, True)

                        # Plusieurs points :
                        #   > Pour qu'une fusion soit accepté, il faut que les deux intervalles
                        #       soit cohérents au niveau du read A et du read B
                        #   > Si deux intervalles sont cohérent uniquement pour le read A et non pour le read B
                        #       ne pas le prendre en compte
                        #   > Si deux intervalles viennent du même fichier, on calcul chacun l'intervalle le plus grand.
                        #       On prend seulement le plus grand
                        #   > Pas le cas ici (gerer le cas ou le premier interval n'est pas le bon)
                        
                        #Il faut reboucler tant que l'on a pas une fusion totale des choses.
                        #A la fin de chaque boucle, tout ce qui n'a pas été fusionné ressort avant.
                        # A B C C.
                        #   > B C C. | A
                        #   > C C. | A ? B
                        #   > C C. B
                        # B C C A
                        #   > C C A. | B
                        #   > C A. | B ? C
                        #   > C A. C | B
                        #   > A. C C |
                        # C C A B
                        # 
                        i_max_run = len(intervals)
                        
                        #Loop to be sure to catch all the possibilities
                        # (In case a interval is not compatible at T0, 
                        #   but is at T1 because the curr_interval would be not the same)
                        for _ in range(0, i_max_run):
                        
                            interval_max = intervals[0]
                            #print(interval_max.toStringInterval())
                            #Retrieves the first element of the list and moves it away
                            curr_list_intervals = []
                            del intervals[0]

                            #Loop until the list is empty
                            while len(intervals) > 0:
                                tmp_interval = intervals[0]
                                del intervals[0]
                                if interval_max.compareAndFusion_gentle(tmp_interval) == 0:
                                    curr_list_intervals.append(tmp_interval)
                            curr_list_intervals.append(interval_max)
                            
                            dict_data[id_a][id_b][strand] = curr_list_intervals
                            intervals = dict_data[id_a][id_b][strand]

        return dict_data              

    def strict_detection(self, dict_data, filespath):
        tools = AnalysisTools()
        for id_a in dict_data:
            for id_b in dict_data[id_a]:
                for strand in dict_data[id_a][id_b]:
                    intervals = dict_data[id_a][id_b][strand]
                    if len(intervals) > 1:
                        intervals = tools.sort_Intervals_start(intervals, True)
                        
                        max_end_value_A = 0
                        max_end_value_B = 0

                        #Get the max end value
                        # Récupération de la valeur de fin minimale
                        for curr_interval in intervals:
                            if curr_interval.getEnd_A() > max_end_value_A:
                                max_end_value_A = curr_interval.getEnd_A()
                            if curr_interval.getEnd_B() > max_end_value_B:
                                max_end_value_B = curr_interval.getEnd_B()

                        #Init the lists
                        #Initialisation des listes pour la courbe de couverture
                        cover_A = []
                        cover_B = []
                        for _ in range(max_end_value_A):
                            cover_A.append([])
                        for _ in range(max_end_value_B):
                            cover_B.append([])
                        
                        #Ajout des intervalles dans les listes
                        for curr_interval in intervals:
                            for i in range (curr_interval.getStart_A(), curr_interval.getEnd_A()):
                                cover_A[i].append(curr_interval)
                            for i in range (curr_interval.getStart_B(), curr_interval.getEnd_B()):
                                cover_B[i].append(curr_interval)

                        #
                        max_interval_A = 0
                        max_interval_B = 0

                        list_id_A = []
                        list_id_B = []
                       
                        #Get max
                        #Récupération de la longueur maximale des listes
                        for i_intervals in cover_A:
                            if len(i_intervals) > max_interval_A: 
                                max_interval_A = len(i_intervals)
                        
                        for i_intervals in cover_B:
                            if len(i_intervals) > max_interval_B: 
                                max_interval_B = len(i_intervals)
                        
                        #Empty the current list of intervals
                        del dict_data[id_a][id_b][strand] [:]
                        
                        #Analyse A
                        # > Vérification que la longueur maximale soit au moins égale au nombre d'overlappers
                        
                        if max_interval_A >= len(filespath) and max_interval_B >= len(filespath):
                            #Treat the several interval case (need more details)
                            
                            #If the function detects several intervals from one overlappers
                            
                            if max_interval_A > len(filespath) or max_interval_A > len(filespath):
                                print("Warning : One or several overlappers created several intervals for one intersection")
                            #Get the intervals list
                            # > Récupération sous la forme de liste de toutes positions avec une longueur maximale ayant au moins un intervalle par overlapper
                            list_id_A = tools.retrieve_id_strict_analysis(filespath, max_interval_A, cover_A, list_id_A)
                            list_id_B = tools.retrieve_id_strict_analysis(filespath, max_interval_B, cover_B, list_id_B)
                            
                            #Vérification que les deux listes se soient pas vides
                            if len(list_id_A) > 0 and len(list_id_B) > 0:
                            
                            #Now almost everything is done. We only need to get the longest interval
                                
                                list_starts_A = []
                                list_ends_A = []
                                list_lengths_A = []
                                list_starts_B = []
                                list_ends_B = []
                                list_lengths_B = []

                                #Parcourt de toutes les positions récupérées. 
                                # Si la position N n'est pas égale à la (position N-1)+1, 
                                # Il s'agit d'un autre intervalle
                                #On récupère donc tous les intervalles disponibles ayant le plus grand consensus
                                curr_length = 0
                                for i in range(len(list_id_A)):
                                    if i == 0:
                                        list_starts_A.append(list_id_A[i])
                                    else:
                                        if list_id_A[i] != (list_id_A[i-1] + 1):
                                            #it's a different interval
                                            list_ends_A.append(list_id_A[i-1])
                                            list_starts_A.append(list_id_A[i])
                                            list_lengths_A.append(curr_length)
                                            curr_length = 0
                                        elif i == len(list_id_A)-1:
                                            curr_length = curr_length + 1
                                            list_ends_A.append(list_id_A[i])
                                            list_lengths_A.append(curr_length)
                                    curr_length = curr_length + 1
                                
                                curr_length = 0

                                for i in range(len(list_id_B)):
                                    if i == 0:
                                        list_starts_B.append(list_id_B[i])
                                    else:
                                        if list_id_B[i] != (list_id_B[i-1] + 1):
                                            #it's a different interval
                                            list_ends_B.append(list_id_A[i-1])
                                            list_starts_B.append(list_id_A[i])
                                            list_lengths_B.append(curr_length)
                                            curr_length = 0
                                        elif i == len(list_id_B)-1:
                                            curr_length = curr_length
                                            list_ends_B.append(list_id_B[i])
                                            list_lengths_B.append(curr_length)
                                    curr_length = curr_length + 1

                                
                                #Guardrail : check if all the lists have the same length
                                #We take the longer intervals among those we found
                                if len(list_starts_A) == len(list_ends_A) and len(list_starts_A) == len(list_lengths_A):
                                    new_interval = Interval("", id_a, id_b, strand, "", "", "", "", "", "")

                                    #Finally check the max
                                    max_length = 0
                                    for i_length in list_lengths_A:
                                        if max_length < i_length:
                                            max_length = i_length
                                    for i in range(len(list_lengths_A)):
                                        if list_lengths_A[i] == max_length:
                                            new_interval.setStart_A(str(list_starts_A[i]))
                                            new_interval.setEnd_A(str(list_ends_A[i]+1))
                                            new_interval.setLength_A(str(list_lengths_A[i]+1))
                                    
                                    for i_length in list_lengths_B:
                                        if max_length < i_length:
                                            max_length = i_length
                                    for i in range(len(list_lengths_B)):
                                        if list_lengths_B[i] == max_length:
                                            new_interval.setStart_B(str(list_starts_B[i]))
                                            new_interval.setEnd_B(str(list_ends_B[i]+1))
                                            new_interval.setLength_B(str(list_lengths_B[i]+1))
                                    
                                    #And add the interval in the dictionnary
                                    dict_data[id_a][id_b][strand].append(new_interval)
                                    
        return dict_data
    
    def statistics(self, dict_data, filespath):
        """Iterates through the triple hashmap of itervals to make some statistics.
        
        Attributes:
            dict_data : the triple hashmap containing the itervals of the overlappers
            nb_input_files : the number of the input files 
        """
        nb_intervals = 0
        nb_connections = 0

        tmp_total = 0.00

        known_types = []

        avg_total_list = []
        avg_total = 0.00

        # avg_coherent_list = []
        # avg_coherent = 0.00
        dict_total = {}
        # dict_total = defaultdict(list)
        list_dict_total = []
        
        # dict_duplicate = defaultdict(list)
        dict_duplicate = {}
        
        for id_a in dict_data:
            for id_b in dict_data[id_a]:
                for strand in dict_data[id_a][id_b]:
                    list_duplicate = []
                    dict_total = {}

                    intervals = dict_data[id_a][id_b][strand]

                    # Count the number of "connections" between two read 2
                    nb_connections += 1

                    # Process the avg intervals per overlap
                    avg_total_list.append(float(len(intervals)))

                    # Iterate through found intervals
                    for i_interval in intervals :

                        i_extension = i_interval.getFilename().split(".")[-1]

                        # Count the number of intervals
                        nb_intervals += 1

                        # Analyse if the extension is known
                        if i_extension not in known_types:
                            known_types.append(i_extension)
                        
                        # Check if 
                        if i_interval.getFilename() not in dict_total:
                            dict_total[i_interval.getFilename()] = 1.00
                        else:
                            dict_total[i_interval.getFilename()] += 1.00
                        
                    list_dict_total.append(dict_total)
                
        file_type_str = ""
        for fileType in known_types :
            file_type_str += fileType + " | "

        # Create the first part of the report (general part)

        if (len(filespath) == 1):
            dep_percent = math.floor( (((sum(avg_total_list)/len(avg_total_list) ) / len(filespath))-1 )* 100) 
        else:
            dep_percent = math.floor( (((sum(avg_total_list)/len(avg_total_list)) -1) / (len(filespath)-1) )* 100) 
        report = ("Report of the program data >>>\n"
        "\tNumber of times there is at least one interval between two reads = " + str(nb_connections) + "\n"
        "\tTotal intervals = " + str(nb_intervals) + "\n"
        "\tKnown file types = " + file_type_str + "\n\n"
        
        "\tAvg of intervals per overlap = " + str(sum(avg_total_list)/len(avg_total_list)) + "\n"
        "\tDependance of percentage of the analysis = " + str(dep_percent)  + "%\n"
        "=========================================================\n"
        "Per file >>>\n"
        )

        # Create the second part of the report (specific part)
        for filepath in filespath :
            filename = filepath.split("/")[-1]
            i_list = []

            for i_dict in list_dict_total:
                if filename in i_dict:
                    i_list.append(float(i_dict[filename]))            
            report += (
            "" + filename + "\n"
            "\tTotal intervals number in this file = " + str(sum(i_list)) + "\n"
            "\tAvg of intervals repetitions in this file = " + str(sum(i_list)/len(i_list)) + "\n"
            )


        return report
        
    def detect_same_overlap(self, intervals):
        pass
                                                              