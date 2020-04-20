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
organized = {}
headers = []
sequences = []
varA = 0
varC = 0
varG = 0
varT = 0

# Loop to parse the muilti-fasta file inside a loop to go through gene name text file
for lines in dnaSequences:
	strings = lines.strip().split('>')
	for i in strings:
		if len(i) == 0:
			continue

		fasta = i.split()
		head = fasta[0]
		seqs = ''.join(fasta[1:])

		organized[head] = seqs

	if lines.startswith(">"):
		headers.append(lines.rstrip())
	else:
		sequences.append(lines.rstrip())

for char in lines:
	if(char == 'A'):
		varA = varA + 1
	elif(char == 'C'):
		varC = varC + 1
	elif(char == 'G'):
		varG = varG + 1
	elif(char == 'T'):
		varT = varT + 1

# Print out the results.
print("Headers List contains: {0} \n Sequence List contains: {1} ".format(headers, sequences))
print(organized)

# Close files to end program
dnaSequences.close()