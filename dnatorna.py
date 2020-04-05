#! usr/bin/env python3.7

import sys
import fileinput

# DNA_Count Python3.7 Script that takes a file from command line arguments 
# and counts the number of A, C, G, T's. Than Prints the output to Standard Out.

# Written by Marcus W. on March 27, 2020

# Welcome to DNA to RNA Program in Python 3.7
# This program takes a .txt file of DNA nucleotides (A,T,C,G) and converts
# the DNA sequence to RNA (A,U,C,G) than prints the new sequence to a file.

# Initialize Variables
varA = 0
varC = 0
varG = 0
varT = 0

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
			print('A', end = "")
		elif(char == 'C'):
			varC = varC + 1
			print('C', end = "")
		elif(char == 'G'):
			varG = varG + 1
			print('G', end = "")
		elif(char == 'T'):
			varT = varT + 1
			print('U', end = "")
print("", end = " ")


print("A = {0} C = {1} G = {2} T = {3}".format(varA, varC, varG, varT))

# Close files to end program
dnaSequence.close()