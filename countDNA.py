#! usr/bin/env python3.7

import sys
import fileinput

# DNA_Count Python3.7 Script that takes a file from command line arguments 
# and counts the number of A, C, G, T's. Than Prints the output to Standard Out.

# Written by Marcus W. on March 26, 2020

# Welcome to DNA count A, C, G, T Program in Python
varA = 0
varC = 0
varG = 0
varT = 0

# Initialize Variables
dna_File = sys.argv[1]
print("The file argument is " + dna_File)

# Open the muilti-fasta file
dnaSequence = open(dna_File)
# print("The sequence is: " + dnaSequence)

print("The program is parsing.")

# Loop to parse the muilti-fasta file inside a loop to go through gene name text file
for lines in dnaSequence:
	for char in lines:
		if(char == 'A'):
			varA = varA + 1
			print(varA)
		elif(char == 'C'):
			varC = varC + 1
			print(varC)
		elif(char == 'G'):
			varG = varG + 1
			print(varG)
		elif(char == 'T'):
			varT = varT + 1
			print(varT)


print("A = {0}. C = {1}. G = {2}. T = {3}".format(varA, varC, varG, varT))

# Close files to end program
dnaSequence.close()