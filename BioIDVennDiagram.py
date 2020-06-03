# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:19:21 2020
@author: Andrew Sydor

To compare BioID Datasets and generate a Venn Diagram 
comparing the two datasets. This script accepts .txt 
files where each line has a separate protein identifier 
listed. 

"""
import pylab as plt
from matplotlib_venn import venn2, venn2_circles

# Opening and reading the files
file1 = "BIOID1"   # Change to file name of file 1, NO FILE EXTENSION
file2 = "BIOID2"    # Change to file name of file 2, NO FILE EXTENSION

f1=open(file1 + ".txt")
f2=open(file2 + ".txt")

f1_contents = f1.readlines()
f1_striped = [item.rstrip("\n") for item in f1_contents]

f2_contents = f2.readlines()
f2_striped = [item.rstrip("\n") for item in f2_contents]

# Creating a new text file for outputting the results
my_file = open(file1 + "_v_" + file2 + ".txt", "w")
my_file.write(f"Common hits between the {file1} and {file2} Datasets\n")

# Comparing the protein hits in the two files
common = set(f1_striped) & set(f2_striped)

# Write the results to file
for line in common:
    my_file.write(line + "\n")

my_file.write(f"\nThere are a total of {len(common)} proteins common between the two datasets.")

# Generate the Venn Diagram
plt.figure(figsize=(5,5))
venn2([set(f1_striped), set(f2_striped)], set_labels = (file1, file2))

# Style changes to the Venn Diagram
c = venn2_circles([set(f1_striped), set(f2_striped)], linestyle='dashed')
c[0].set_lw(2.0)
c[0].set_ls('dashed')
plt.show()

# Close files
my_file.close()    
f1.close()
f2.close()
