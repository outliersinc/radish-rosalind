#! usr/bin/env python3.7

import sys
import fileinput

# pointMutations.py is a Python3.7 Script that takes a file from command line arguments
# Prints the output to Standard Out.

# Written by Marcus W. on April 13, 2020

# Welcome to Point Mutation hunting in DNA Python 3.7 Program
# This program takes a .txt file of DNA nucleotides (A,T,C,G).

seq_File = sys.argv[1]
print("The file argument is " + seq_File)

# Open the muilti-fasta file
dnaSequence = open(seq_File)

# Loop through dnaSequence file and store sequence 1 to string1.
# Loop through dnaSequence file and store sequence 2 to string2.

# Initialize variables
countMutation = 0
loop = 0
splitFile = dnaSequence.readlines()
dnaSeq1 = splitFile[0]
print("dnaSeq1 contains: " + dnaSeq1)
dnaSeq2 = splitFile[1]
print("dnaSeq2 contains: " + dnaSeq2)

seq1Length = len(dnaSeq1)
seq2Length = len(dnaSeq2)

while seq1Length > 0:
    print("The loop count is: {0} amd the countMutation is {1}".format(loop, countMutation))
    if dnaSeq1[loop] != dnaSeq2[loop]:
        countMutation += 1
    seq1Length -= 1
    loop += 1

print("The number of mutations aka the Hamming distance is: {0}".format(countMutation))

# Close files to end program
dnaSequence.close()