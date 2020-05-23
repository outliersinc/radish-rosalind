#! usr/bin/env python3.7

import sys

# mRNA Program involves the Translation of Protein to RNA using Python3.7 Script that takes a file from command line arguments
#  Than Prints the output to Standard Out.

# Written by Marcus W. on May 15, 2020

# Welcome to DNA to RNA Program in Python 3.7
# This program takes a .txt file of RNA nucleotides (A,U,C,G) and translates
# the RNA sequence to Protein then prints the new sequence to a file.

# UUU F      CUU L      AUU I      GUU V
# UUC F      CUC L      AUC I      GUC V
# UUA L      CUA L      AUA I      GUA V
# UUG L      CUG L      AUG M      GUG V
# UCU S      CCU P      ACU T      GCU A
# UCC S      CCC P      ACC T      GCC A
# UCA S      CCA P      ACA T      GCA A
# UCG S      CCG P      ACG T      GCG A
# UAU Y      CAU H      AAU N      GAU D
# UAC Y      CAC H      AAC N      GAC D
# UAA Stop   CAA Q      AAA K      GAA E
# UAG Stop   CAG Q      AAG K      GAG E
# UGU C      CGU R      AGU S      GGU G
# UGC C      CGC R      AGC S      GGC G
# UGA Stop   CGA R      AGA R      GGA G
# UGG W      CGG R      AGG R      GGG G

# open the file
try:
    dna_File = sys.argv[1]
    dnaSeq = open(dna_File)
except:
    dnaSeq = open('test.txt', 'r')

# Initialize variables
aa = ""
aa2 = ""
codonF1 = ""
codonF2 = ""
codonR1 = ""
codonR2 = ""
seqList = []
newSeqList = []
count = 1
protein = ""
protF1 = []
protF2 = []
protR1 = []
protR2 = []
dict = {'TTT': 'F',
        'TTC': 'F',
        'TTA': 'L',
        'TTG': 'L',
        'TCT': 'S',
        'TCC': 'S',
        'TCA': 'S',
        'TCG': 'S',
        'TAT': 'Y',
        'TAC': 'Y',
        'TAA': 'Stop',
        'TAG': 'Stop',
        'TGT': 'C',
        'TGC': 'C',
        'TGA': 'Stop',
        'TGG': 'W',
        'CTT': 'L',
        'CTC': 'L',
        'CTA': 'L',
        'CTG': 'L',
        'CCT': 'P',
        'CCC': 'P',
        'CCA': 'P',
        'CCG': 'P',
        'CAT': 'H',
        'CAC': 'H',
        'CAA': 'Q',
        'CAG': 'Q',
        'CGT': 'R',
        'CGC': 'R',
        'CGA': 'R',
        'CGG': 'R',
        'ATT': 'I',
        'ATC': 'I',
        'ATA': 'I',
        'ATG': 'M',
        'ACT': 'T',
        'ACC': 'T',
        'ACA': 'T',
        'ACG': 'T',
        'AAT': 'N',
        'AAC': 'N',
        'AAA': 'K',
        'AAG': 'K',
        'AGT': 'S',
        'AGC': 'S',
        'AGA': 'R',
        'AGG': 'R',
        'GTT': 'V',
        'GTC': 'V',
        'GTA': 'V',
        'GTG': 'V',
        'GCT': 'A',
        'GCC': 'A',
        'GCA': 'A',
        'GCG': 'A',
        'GAT': 'D',
        'GAC': 'D',
        'GAA': 'E',
        'GAG': 'E',
        'GGT': 'G',
        'GGC': 'G',
        'GGA': 'G',
        'GGG': 'G' }

# Loop to parse the DNA Sequence inside a loop to go through gene name text file
for lines in dnaSeq:
    for char in range(0,len(lines)-1, 3):
        codonF1 = lines[char] + lines[char+1] + lines[char+2]
        codonF2 = lines[char+1] + lines[char+2] + lines[char+3]
        count += 1
        aa = dict[codonF1]
        protF1.append(aa)
        aa2 = dict[codonF2]
        protF2.append(aa2)
        if aa == "Stop" | aa2 == "Stop":
            pass
        else:
            protein += aa

# Take the string dnaSeqString and copy the contents into a list called seqList.
for char in dnaSeqStr:
    if(char == 'A'):
        #print('T', end = " ")
        seqList.append('T')
    elif(char == 'C'):
        #print('G', end = " ")
        seqList.append('G')
    elif(char == 'G'):
        #print('C', end = " ")
        seqList.append('C')
    elif(char == 'T'):
        #print('A', end = " ")
        seqList.append('A')
print(" ")

# Flip the contents of seqList into newseqList
newseqList = seqList[::-1]

# Print to see if the lists (seqList, newseqList) are empty.
print(seqList)
print(newseqList)

for i in newseqList:
    codonF1 = lines[char] + lines[char + 1] + lines[char + 2]
    codonF2 = lines[char + 1] + lines[char + 2] + lines[char + 3]
    print(codonF1)
    print(codonF2)
    print(aa)
    print(aa2)
    count += 1
    aa = dict[codonF1]
    protF1.append(aa)
    aa2 = dict[codonF2]
    protF2.append(aa2)
    if aa == "Stop" | aa2 == "Stop":
        pass
    else:
        protein += aa
print(" ")

def compliment(dnaList):
    seqList = []
    reverseList = []
    for char in dnaList:
        if(char == 'A'):
            seqList.append('T')
        elif(char == 'C'):
            seqList.append('G')
        elif(char == 'G'):
            seqList.append('C')
        elif(char == 'T'):
            seqList.append('A')
    print(" ")
    newseqList = seqList[::-1]

    return reverseList;

def translate(seqList):
    protList = []
    F1 = ""
    aa = ""
    for char in seqlist:
        F1 = lines[char] + lines[char + 1] + lines[char + 2]
        aa = dict[F1]
        protList.append(aa)
        if aa == "Stop" | aa2 == "Stop":
            pass
        else:
            protein += aa

# Print the output.
print("The protein is {0} and the count is {1}".format(protein, count))
print("The protein is {0} and the count is {1}".format(protein, count))
# Print the output.

# Close files to end program
dnaSeq.close()