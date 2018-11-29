import sys
import math
from collections import defaultdict
from Parameters import Parameters
from ReadFiles import ReadFiles
from IteratorTools import *


class Iterator:
    def detect_overlaps(self, dict_data, strict):
        pass
        """
        processed_dict_data = {}
        # Loop on all the data
        for id_a in dict_data:
            for id_b in dict_data[id_a]:

                # Retrieve the interval list
                intervals = dict_data[id_a][id_b]
                # print(len(intervals))

                # If the interval list has more than 1 element (possible same overlap)

                # S'il n'y a qu'un seul intervalle, on le supprime(?)
                if len(intervals) > 1 :
                    # Plusieurs cas
                    # Mise en place d'un compteur à 1


                    # Si la différence est trop grande (avec une marge de manoeuvre),
                    #   on ne crée pas de nouvel intervalle (et donc les intervalles sont supprimés)
                    #   on incrémente le compteur si les fichiers des deux intervals sont différents

                    # S'il y a une concordance, on prend l'écart le plus petit

                    # Si le compteur est égal ou supérieur au nombre d'overlappers minium, on ajoute l'interval à la liste.
                    #   Sinon, rien ne se fait
                    # Garde

                    new_interval = intervals[0]
                    del intervals[0]

                    # while len(intervals) > 0:
        """
        for id_a in dict_data:
            for id_b in dict_data[id_a]:
                intervals = dict_data[id_a][id_b]
                if strict is True:
                    pass
                else:
                    pass

    def gentle_detection(self, dict_data):
        tools = IteratorTools()
        for id_a in dict_data:
            for id_b in dict_data[id_a]:
                intervals = dict_data[id_a][id_b]
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
                    interval_max = intervals[0]
                    #Retrieves the first element of the list and moves it away
                    new_intervals = []
                    del intervals[0]

                    #Loop until the list is empty
                    while len(intervals) > 0:
                        tmp_interval = intervals[0]
                        del intervals[0]

                        
                        #(test)
                        
                        if id_a == '1' and id_b == '6696':
                            print("=-=")
                            for i_interval in dict_data['1']['6696']:
                                print(i_interval.toStringInterval())
                            
                            print(interval_max.getEnd_A(), " VS ", tmp_interval.getStart_A(), " Du coup : ", interval_max.getEnd_A() >= tmp_interval.getStart_A())

                        #Beginning of the interval fusion
                        if interval_max.getEnd_A() >= tmp_interval.getStart_A():
                        
                            if id_a == '1' and id_b == '6696':
                                print("COUCOU")
    
                            if (interval_max.getEnd_B() >= tmp_interval.getStart_B()) or (interval_max.getStart_B() <= tmp_interval.getEnd_B()):
                                
                                if id_a == '1' and id_b == '6696':
                                    print("AVANT INTERVAL ", interval_max.toStringInterval())
                                
                                interval_max.setStart_A(
                                   min(interval_max.getStart_A(), tmp_interval.getStart_A()))
                                interval_max.setStart_B(
                                   min(interval_max.getStart_B(), tmp_interval.getStart_B()))

                                interval_max.setEnd_A(
                                   max(interval_max.getEnd_A(), tmp_interval.getEnd_A()))
                                interval_max.setEnd_B(
                                   max(interval_max.getEnd_B(), tmp_interval.getEnd_B()))

                                if id_a == '1' and id_b == '6696':
                                    print("APRES INTERVAL ", interval_max.toStringInterval())
                            else:
                                pass
                                #new_intervals.append(tmp_interval)
                        else:
                            pass
                            #new_intervals.append(tmp_interval)       
                    new_intervals.append(interval_max)
                    
                    dict_data[id_a][id_b] = new_intervals

        return dict_data              

    def strict_detection(self, dict_data):
        pass
    
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
                list_duplicate = []
                dict_total = {}

                intervals = dict_data[id_a][id_b]

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

                    if i_interval.getFilename() not in dict_total:
                        dict_total[i_interval.getFilename()] = 1.00
                    else:
                        dict_total[i_interval.getFilename()] += 1.00
                    
                list_dict_total.append(dict_total)
                
        file_type_str = ""
        for fileType in known_types :
            file_type_str += fileType + " | "

        # Create the first part of the report (general part)
        report = ("Report of the program data >>>\n"
        "\tTotal different connections between two reads = " + str(nb_connections) + "\n"
        "\tTotal intervals = " + str(nb_intervals) + "\n"
        "\tKnown file types = " + file_type_str + "\n\n"
        
        "\tAvg of intervals per overlap = " + str(sum(avg_total_list)/len(avg_total_list)) + "\n"
        "\tDependance of percentage of the analysis = " + str(math.floor( (((sum(avg_total_list)/len(avg_total_list))-1 ) / len(filespath) )* 100) )  + "%\n"
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
