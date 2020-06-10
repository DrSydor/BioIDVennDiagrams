# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 11:19:21 2020
@author: Andrew Sydor

To compare a BioID Dataset with multiple baits to one with a single bait and 
generate Venn Diagrams comparing the two datasets. This script accepts .txt 
files where each line has a separate bait-prey interaction listed. 

"""
import pylab as plt
from matplotlib_venn import venn2, venn2_circles
from collections import defaultdict

# Opening and reading the files; DO NOT INCLUDE FILE EXTENSIONS
file1 = "OSBPLBioID2"   # File name of file 1 (multiple baits)
file2 = "ER-Mitochondria MCS"    # File name of file 2

dict1 = defaultdict(list)

with open(file1 + ".txt") as f1:
    for line in f1:
        if line.strip():
            a,b =  line.strip().split()
            dict1[a].append(b)

with open(file2 + ".txt") as f2:
    f2_contents = f2.readlines()
    f2_striped = [item.rstrip("\n") for item in f2_contents]

# Creating a new text file for outputting the results
my_file = open("Common hits- " + file1 + " v " + file2 + ".txt", "w")
my_file.write(f"Common hits between the {file1} and {file2} Datasets\n\n")

# Comparing the protein hits in the two files
for key in dict1.keys():
    common = set(dict1[key]) & set(f2_striped)
    # Write the results to file
    common_sorted = list(common)
    common_sorted.sort()
    my_file.write("Comparing " + key + " vs " + file2 + ":\n")
    for line in common_sorted:
        my_file.write(line + "\n")
    my_file.write(f"There are a total of {len(common)} proteins common between the two datasets.\n\n")

# Generate the Venn Diagrams
for key in dict1.keys():
    plt.figure(figsize=(5,5))
    venn2([set(dict1[key]), set(f2_striped)], set_labels = (key, file2))
    # Style changes to the Venn Diagram
    c = venn2_circles([set(dict1[key]), set(f2_striped)], linestyle='dashed')
    c[0].set_lw(2.0)
    c[0].set_ls('dashed')
    plt.show()

# Close files
my_file.close()    
