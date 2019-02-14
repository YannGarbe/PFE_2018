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
from misc.MyWarnings import *

"""This class implements the custom, max, and strict analyses"""
class CoverageTypeAnalysis:

    def analyse_data(self, dict_data, filespath, analysis_type, custom_type_value, get_all):
        tools = AnalysisTools()
        for id_a in dict_data:
            for id_b in dict_data[id_a]:
                for strand in dict_data[id_a][id_b]:
                    intervals = dict_data[id_a][id_b][strand]
                    if len(intervals) > 1:
                        intervals = tools.remove_duplicates_interval(tools.sort_Intervals_start(intervals, True))

                        max_end_value_A = 0
                        max_end_value_B = 0

                        # Get the max end value
                        # Récupération de la valeur de fin minimale
                        for curr_interval in intervals:
                            if curr_interval.getEnd_A() > max_end_value_A:
                                max_end_value_A = curr_interval.getEnd_A()
                            if curr_interval.getEnd_B() > max_end_value_B:
                                max_end_value_B = curr_interval.getEnd_B()

                        # Init the lists
                        # Initialisation des listes pour la courbe de couverture
                        cover_A = []
                        cover_B = []
                        for _ in range(max_end_value_A):
                            cover_A.append([])
                        for _ in range(max_end_value_B):
                            cover_B.append([])

                        # Ajout des intervalles dans les listes
                        for curr_interval in intervals:
                            for i in range(curr_interval.getStart_A(), curr_interval.getEnd_A()):
                                cover_A[i].append(curr_interval)
                            for i in range(curr_interval.getStart_B(), curr_interval.getEnd_B()):
                                cover_B[i].append(curr_interval)

                        list_id_A = []
                        list_id_B = []

                        # Get max
                        # Récupération de la longueur maximale des listes
                        if analysis_type < 10:
                            max_interval_A = 0
                            max_interval_B = 0
                            for i_intervals in cover_A:
                                if len(i_intervals) > max_interval_A:
                                    max_interval_A = len(i_intervals)

                            for i_intervals in cover_B:
                                if len(i_intervals) > max_interval_B:
                                    max_interval_B = len(i_intervals)

                        # Empty the current list of intervals
                        del dict_data[id_a][id_b][strand][:]



                        #Check the analysis. If the type is a Strict analysis, we need to check if the max found is equals to the number of the overlappers
                        if (analysis_type != 0) or (max_interval_A == len(filespath) and max_interval_B == len(filespath)):
                           # Get the intervals list 
                            if analysis_type == 0:
                                list_id_A = tools.retrieve_id_strict_analysis(filespath, max_interval_A, cover_A, list_id_A)
                                list_id_B = tools.retrieve_id_strict_analysis(filespath, max_interval_B, cover_B, list_id_B)
                            elif analysis_type == 1:
                                list_id_A = tools.retrieve_id_equals_analysis(max_interval_A, cover_A, list_id_A)
                                list_id_B = tools.retrieve_id_equals_analysis(max_interval_B, cover_B, list_id_B)
                            elif analysis_type > 10:
                                if analysis_type == 11:
                                    list_id_A = tools.retrieve_id_more_analysis(custom_type_value, cover_A, list_id_A)
                                    list_id_B = tools.retrieve_id_more_analysis(custom_type_value, cover_B, list_id_B)
                                elif analysis_type == 12:
                                    list_id_A = tools.retrieve_id_less_analysis(custom_type_value, cover_A, list_id_A)
                                    list_id_B = tools.retrieve_id_less_analysis(custom_type_value, cover_B, list_id_B)
                                else:
                                    list_id_A = tools.retrieve_id_equals_analysis(custom_type_value, cover_A, list_id_A)
                                    list_id_B = tools.retrieve_id_equals_analysis(custom_type_value, cover_B, list_id_B)
                            # Vérification que les deux listes se soient pas vides
                            if len(list_id_A) > 0 and len(list_id_B) > 0:

                            # Now almost everything is done. We only need to get the longest interval

                                list_starts_A = []
                                list_ends_A = []
                                list_lengths_A = []
                                list_starts_B = []
                                list_ends_B = []
                                list_lengths_B = []

                                # Parcourt de toutes les positions récupérées.
                                # Si la position N n'est pas égale à la (position N-1)+1,
                                # Il s'agit d'un autre intervalle
                                # On récupère donc tous les intervalles disponibles ayant le plus grand consensus
                                curr_length = 0
                                for i in range(len(list_id_A)):
                                    if i == 0:
                                        list_starts_A.append(list_id_A[i])
                                    else:
                                        if list_id_A[i] != (list_id_A[i-1] + 1):
                                            # it's a different interval
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
                                            # it's a different interval
                                            list_ends_B.append(list_id_A[i-1])
                                            list_starts_B.append(list_id_A[i])
                                            list_lengths_B.append(curr_length)
                                            curr_length = 0
                                        elif i == len(list_id_B)-1:
                                            curr_length = curr_length
                                            list_ends_B.append(list_id_B[i])
                                            list_lengths_B.append(curr_length)
                                    curr_length = curr_length + 1
                                    
                                # Guardrail : check if all the lists have the same length
                                # We take the longer intervals among those we found
                                
                                if len(list_starts_A) == len(list_ends_A) and len(list_starts_A) == len(list_lengths_A):
                                    if get_all:
                                        new_list_interval=[]
                                        if len(list_starts_A) >= len(list_starts_B):
                                            
                                            for i in range(len(list_lengths_B)):
                                                new_interval=Interval(
                                                    "", id_a, id_b, strand, "", "", "", "", "", "")
                                                
                                                new_interval.setStart_A(
                                                    str(list_starts_A[i]))
                                                new_interval.setEnd_A(
                                                    str(list_ends_A[i]+1))
                                                new_interval.setLength_A(
                                                    str(list_lengths_A[i]+1))
                                                
                                                
                                                new_interval.setStart_B(
                                                    str(list_starts_B[i]))
                                                new_interval.setEnd_B(
                                                    str(list_ends_B[i]+1))
                                                new_interval.setLength_B(
                                                    str(list_lengths_B[i]+1))
                                                new_list_interval.append(new_interval)

                                        else:
                                            
                                            for i in range(len(list_lengths_A)):
                                                new_interval=Interval(
                                                    "", id_a, id_b, strand, "", "", "", "", "", "")
                                                
                                                new_interval.setStart_A(
                                                    str(list_starts_A[i]))
                                                new_interval.setEnd_A(
                                                    str(list_ends_A[i]+1))
                                                new_interval.setLength_A(
                                                    str(list_lengths_A[i]+1))
                                                
                                                
                                                new_interval.setStart_B(
                                                    str(list_starts_B[i]))
                                                new_interval.setEnd_B(
                                                    str(list_ends_B[i]+1))
                                                new_interval.setLength_B(
                                                    str(list_lengths_B[i]+1))
                                                new_list_interval.append(new_interval)
                                        
                                        dict_data[id_a][id_b][strand] = new_list_interval

                                    else:

                                        new_interval=Interval(
                                            "", id_a, id_b, strand, "", "", "", "", "", "")

                                        # Finally check the max
                                        # Get the longest interval
                                        max_length=0
                                        for i_length in list_lengths_A:
                                            if max_length < i_length:
                                                max_length=i_length
                                        for i in range(len(list_lengths_A)):
                                            if list_lengths_A[i] == max_length:
                                                new_interval.setStart_A(
                                                    str(list_starts_A[i]))
                                                new_interval.setEnd_A(
                                                    str(list_ends_A[i]+1))
                                                new_interval.setLength_A(
                                                    str(list_lengths_A[i]+1))

                                        for i_length in list_lengths_B:
                                            if max_length < i_length:
                                                max_length=i_length
                                        for i in range(len(list_lengths_B)):
                                            if list_lengths_B[i] == max_length:
                                                new_interval.setStart_B(
                                                    str(list_starts_B[i]))
                                                new_interval.setEnd_B(
                                                    str(list_ends_B[i]+1))
                                                new_interval.setLength_B(
                                                    str(list_lengths_B[i]+1))

                                        # And add the interval in the dictionnary
                                        dict_data[id_a][id_b][strand].append(
                                            new_interval)
                                else:
                                    raise UnknownError("Unexcpected Error : ", len(list_starts_A), ", ", len(
                                        list_ends_A), " and ", len(list_lengths_A), " should have been equal.")
                        elif max_interval_A > len(filespath) or max_interval_B > len(filespath):
                            warning_max_interval_greater_than_length_overlappers(intervals, filespath)
        return dict_data
