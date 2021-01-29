"""
Created on Sat Sept 5 2020
@author: Andrew Sydor

To compare a BioID Dataset with multiple baits to one with a single bait and 
generate Venn Diagrams comparing the two datasets. This script accepts .txt 
files where each line has a separate bait-prey interaction listed. Saves the
resulting Venn Diagrams and list of common proteins as a PDF file. (V5)

"""
import pylab as plt
from matplotlib_venn import venn2
from collections import defaultdict
from matplotlib.backends.backend_pdf import PdfPages

def retFig(key, key2):
    '''
    This function will find all the common proteins between the two BioID
    datasets and return a figure containing both a venn diagram of the common
    proteins, but also a short text segment indicating the number of common
    proteins and the names of the common proteins.

    '''
    # Identification of the common proteins between the two datasets
    common = set(dict1[key]) & set(dict2[key2])
    common_sorted = list(common)
    common_sorted.sort()
    figtxt = " "
    figtxt2 = figtxt.join(common_sorted)
    
    # Generation of the Venn diagram
    c = plt.figure(figsize=(10,10))
    plt.title("Comparing " + key + " vs " + key2 + " BioID Datasets:", fontname="Helvetica", fontsize=18, fontweight='bold')
    txt = "There are a total of " + str(len(common)) + " proteins common between the two datasets.\n Common: " + TextWrap(figtxt2, 70)
    plt.text(0.05,0.07,txt, transform=c.transFigure, size=10)
    venn2([set(dict1[key]), set(dict2[key2])], set_labels = (key, key2))
    plt.close()
    return c

def TextWrap(string, txt_len):
    '''
    This function wraps text to a certain length, given by the variable txt_len.
    The function will only wrap text at a space and will continue to search for 
    a space (in the forward direction of the string) until one is found.

    '''
    stri_wrap = ""
    n = txt_len -1
    stri_len = len(string)
    
    '''
    The while loop will keep looking for spaces in the string. If no space
    is found at the given string length, an additional length of 1 is added and\
    it tries to see if a space is located at that position. It keeps repeating
    until a space if found, at which point it then appends the string up to that
    point on to the text-wrapped string (stri_wrap) and then redefines the original
    string as the remaining string past that point. It then repeats as long as the
    original string length is more than the desired length (given by txt_len).
    '''
    while stri_len > txt_len:
        print(key)
        print(key2)
        print(n)
        if n >= len(string):
            stri_wrap += string[0:n+1]
            break
        elif string[n] == " ":
            stri_wrap += string[0:n+1]
            stri_wrap += "\n"
            string = string[n:]
            n = txt_len
            stri_len = len(string)
        else:
            n += 1
    
    # The following appends the remaining string on the text-wrapped string.
    stri_wrap += string[0:]
    
    return stri_wrap
         
# Opening and reading the files; DO NOT INCLUDE FILE EXTENSIONS
file1 = "File_Name1"   # File name of file 1 (multiple baits)
file2 = "File_Name2"    # File name of file 2

dict1 = defaultdict(list)
dict2 = defaultdict(list)

with open(file1 + ".txt") as f1:
    for line in f1:
        if line.strip():
            a,b =  line.strip().split()
            dict1[a].append(b)
            
with open(file2 + ".txt") as f2:
    for line in f2:
        if line.strip():
            a,b =  line.strip().split()
            dict2[a].append(b)

# Creating a new pdf file for outputting the results
filename = "Common hits- " + file1 + " v " + file2 + ".pdf"
pdf = PdfPages(filename)

# Generate the Venn Diagrams and save to PDF
for key in dict1.keys():
    for key2 in dict2.keys():
        pdf.savefig(retFig(key, key2))

# Close files
pdf.close()
f1.close()
f2.close()
