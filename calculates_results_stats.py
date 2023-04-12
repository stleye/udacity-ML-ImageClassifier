#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#
# PROGRAMMER: Sebastian Tleye
# DATE CREATED: 04/08/2023
# REVISED DATE:
# PURPOSE: Create a function calculates_results_stats that calculates the
#          statistics of the results of the programrun using the classifier's model
#          architecture to classify the images. This function will use the
#          results in the results dictionary to calculate these statistics.
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best'
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the
#          how to calculate the counts and percentages for this function.
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics
#          (either a percentage or a count) where the key is the statistic's
#           name (starting with 'pct' for percentage or 'n' for count) and value
#          is the statistic's value.  This dictionary should contain the
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model
    architecture to classifying pet images. Then puts the results statistics in a
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet Image 'is-NOT-a' dog.
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """

    Z, A, B, C, D, E, Y = 0, 0, 0, 0, 0, 0, 0

    for key, value in results_dic.items():
        Z += 1  # Z - Number of Images

        if value[3] == 1 and value[4] == 1:
            A += 1  # A - Number of Correct Dog matches

        if value[3] == 1:  # B - Number of Dog Images
            B += 1

        if value[3] == 0 and value[4] == 0:  # C - Number of Correct Non-Dog matches
            C += 1

        if value[3] == 0:  # D - Number of Not Dog Images
            D += 1

        if value[2] == 1 and value[3] == 1:  # E - Number of Correct Breed matches
            E += 1

        if value[2] == 1:  # Y - Number of Label matches
            Y += 1

    objective_1_a = A/B * 100 if B > 0 else 0
    objective_1_b = C/D * 100 if D > 0 else 0
    objective_2 = E/B * 100 if B > 0 else 0
    objective_optional = Y/Z * 100 if Z > 0 else 0

    result = dict({'n_images': Z,
                   'n_dogs_img': B,
                   'n_notdogs_img': D,
                   'n_correct_dogs': A,
                   'n_correct_notdogs': C,
                   'n_correct_breed': E,
                   'n_labels_match': Y,
                   'pct_correct_dogs': objective_1_a,
                   'pct_correct_notdogs': objective_1_b,
                   'pct_correct_breed': objective_2,
                   'pct_correct_label_matches': objective_optional})

    return result
