import sys
from collections import defaultdict
from Parameters import Parameters
from ReadFiles import ReadFiles


class Iterator:
    def detect_overlaps (self, dict_data):
        pass
        """
        processed_dict_data = {}
        #Loop on all the data
        for id_a in dict_data:
            for in_b in dict_data[id_a]:
                
                #Retrieve the interval list
                intervals = dict_data[id_a][in_b]
                #print(len(intervals))

                #If the interval list has more than 1 element (possible same overlap)
                
                #S'il n'y a qu'un seul intervalle, on le supprime(?)
                if len(intervals) > 1 :
                    #Plusieurs cas
                    #Mise en place d'un compteur à 1
                    

                    #Si la différence est trop grande (avec une marge de manoeuvre),
                    #   on ne crée pas de nouvel intervalle (et donc les intervalles sont supprimés)
                    #   on incrémente le compteur si les fichiers des deux intervals sont différents
                    
                    #S'il y a une concordance, on prend l'écart le plus petit

                    #Si le compteur est égal ou supérieur au nombre d'overlappers minium, on ajoute l'interval à la liste.
                    #   Sinon, rien ne se fait
                    # Garde 
                    
                    new_interval = intervals[0]
                    del intervals[0]

                    #while len(intervals) > 0:
        """
    def statistics(self, dict_data, filespath):
        """Iterates through the double hashmap of itervals to make some statistics.
        
        Attributes:
            dict_data : the double hashmap containing the itervals of the overlappers
            nb_input_files : the number of the input files 
        """
        nb_intervals = 0
        nb_connections = 0

        tmp_total = 0.00

        known_types = []

        avg_total_list = []
        avg_total = 0.00

        #avg_coherent_list = []
        #avg_coherent = 0.00
        dict_total = {}
        #dict_total = defaultdict(list)
        list_dict_total = []
        
        #dict_duplicate = defaultdict(list)
        dict_duplicate = {}
        
        for id_a in dict_data:
            for in_b in dict_data[id_a]:
                list_duplicate = []
                dict_total = {}

                intervals = dict_data[id_a][in_b]

                #Count the number of "connections" between two read 2
                nb_connections += 1

                #Process the avg intervals per overlap
                avg_total_list.append(float(len(intervals)))

                #Iterate through found intervals
                for i_interval in intervals :
                    
                    i_extension = i_interval.getFilename().split(".")[-1]

                    #Count the number of intervals
                    nb_intervals += 1

                    #Analyse if the extension is known
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

        #Create the first part of the report (general part)
        report = ("Report of the program data >>>\n"
        "\tTotal different connections between two reads = " + str(nb_connections) + "\n"
        "\tTotal intervals = " + str(nb_intervals) + "\n"
        "\tKnown file types = " + file_type_str + "\n\n"
        
        "\tAvg of intervals per overlap = " + str(sum(avg_total_list)/len(avg_total_list)) + "\n"
        "=========================================================\n"
        "Per file >>>\n"
        )

        #Create the second part of the report (specific part)
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