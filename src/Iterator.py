import sys
from collections import defaultdict
from Parameters import Parameters
from ReadFiles import ReadFiles

class Iterator:
    def detect_overlaps (self, dict_data):

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

    def statistics(self, dict_data, nb_input_files):
        """Iterates through the double hashmap of itervals to make some statistics.
        
        Attributes:
            dict_data : the double hashmap containing the itervals of the overlappers
            nb_input_files : the number of the input files 
        """

        avg_total = 0.00
        avg_coherent = 0.00
        avg_duplicate = 0.00

        #dict_total = defaultdict(list)
        dict_total = {}
        #dict_coherent = defaultdict(list)
        dict_coherent = {}
        #dict_duplicate = defaultdict(list)
        dict_duplicate = {}
        for id_a in dict_data:
            for in_b in dict_data[id_a]:
                intervals = dict_data[id_a][in_b]
                map_duplicate = {}

                if avg_total == 0.00:
                        avg_total = float(len(intervals))
                        avg_coherent = (float(len(intervals)) / nb_input_files)

                else :
                    avg_total += float(len(intervals))
                    avg_coherent += (float(len(intervals)) / nb_input_files)
                    avg_total = avg_total / 2
                    avg_coherent = avg_coherent / 2
                
                for i_interval in intervals :
                    if i_interval.getFilename() not in map_duplicate:
                        map_duplicate[i_interval.getFilename()] = 1
                    else:
                        map_duplicate[i_interval.getFilename()] = map_duplicate[i_interval.getFilename()] + 1


                

                """
                if len(intervals) == 1 :
                    
                    if avg_total == 0.00:
                        avg_total = (1.00 / nb_input_files)
                        avg_coherent = (1.00 / nb_input_files)
                    else :
                        avg_total += (1.00 / nb_input_files)
                        avg_coherent += (1.00 / nb_input_files)
                        avg_total = avg_total / 2
                        avg_coherent = avg_coherent / 2
                """
        report = ("Moyenne totale d'intervalles par read : " + str(avg_total) + "\n" #+ dict_total + ""
        "avg_coherent " + str(avg_coherent) + "\n" #+ dict_coherent + ""
        "avg_duplicate " + str(avg_duplicate) + "\n") #+ dict_duplicate + "")

        return report
        
    def detect_same_overlap(self, intervals):
        pass