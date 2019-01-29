import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from read.Parameters import Parameters
from read.ReadFiles import ReadFiles
from misc.AnalysisTools import *
from misc.Interval import *


class GentleAnalysis:

    def analyse_data(self, dict_data):
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
