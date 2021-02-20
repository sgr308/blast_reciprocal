# Import modules.
import os, re, sys

# Define output file.
out_file = open("blast_reciprocal_result.txt", "w+")

# Import first blast file.
blast_file_1 = open("blastresults_1.txt","r")

# Read first column (query) and second column (reference). Split the first column by "." and take only top-hit result.
#Create a dictionary with first column data as key and second column data as value.

blast_dict1 = {}

blast_key_list1 = []

for line in blast_file_1:
        blast_dict1_key=line.split()[0].split(".")[0]
        blast_dict1_value=line.split()[1]
        if blast_dict1_key in blast_key_list1:
                continue
        blast_key_list1.append(blast_dict1_key)
        blast_dict1[blast_dict1_key]=blast_dict1_value

# Import second blast file.
blast_file_2 = open("blastresults_2.txt","r")

# Read first column (query) and second column (reference). Split the second column by "." and take only top-hit result.
#Create a dictionary with first column data as key and second column data as value.

blast_dict2 = {}

blast_key_list2 = []

for line1 in blast_file_2:
        blast_dict2_key=line1.split()[0]
        blast_dict2_value=line1.split()[1].split(".")[0]
        if blast_dict2_key in blast_key_list2:
                continue
        blast_key_list2.append(blast_dict2_key)
        blast_dict2[blast_dict2_key]=blast_dict2_value

# Check if the keys and values of the dictionary one is not in the dictionary two, if not found then continue.
#Then check if dictionary two's keys and dictionary one's keys are matched or not then print keys and values of dictionary one.

for key1, value1 in blast_dict1.items():
        if blast_dict1[key1] not in blast_dict2.keys():
                continue
        if blast_dict2[blast_dict1[key1]] == key1:
                print >> out_file, key1, value1
