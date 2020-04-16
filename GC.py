#! usr/bin/env python3.7

import sys
import fileinput

# GC Content Python3.7 Script that takes a file from command line arguments
# and counts the number of A, C, G, T's than figures out % GC.
# Than Prints the output to Standard Out.

# Written by Marcus W. on April 15, 2020

# Read in File from Command Line using argv.
fasta_File = sys.argv[1]
print("The file argument is " + fasta_File)

# Open the muilti-fasta file
dnaSequences = open(fasta_File)

# Initialize Variables
seqList = []
fullList = []
varA = 0
varC = 0
varG = 0
varT = 0

# Loop to parse the muilti-fasta file inside a loop to go through gene name text file
for lines in dnaSequences:
	for char in lines:
		fullList.append(char)
		if(char == 'A'):
			varA = varA + 1
			seqList.append('A')
		elif(char == 'C'):
			varC = varC + 1
			seqList.append('C')
		elif(char == 'G'):
			varG = varG + 1
			seqList.append('G')
		elif(char == 'T'):
			varT = varT + 1
			seqList.append('T')

print("The full list is {0} with {1} >'s".format(fullList, fullList.count('>')))
print("The seq list is {0} with {1} >'s".format(seqList, seqList.count('>')))

# Close files to end program
dnaSequences.close()