#! usr/bin/env python3.7

import sys
import fileinput

# DNA_Count Python3.7 Script that takes a file from command line arguments
# Prints the output to Standard Out.

# Written by Marcus W. on March 31, 2020

# Welcome to Motif Hunting in DNA Python 3.7 Program
# This program takes a .txt file of DNA nucleotides (A,T,C,G) and a motif file.
# The file than takes the motif and records all the starting nucleotide locations in the file.

seq_File = sys.argv[1]
print("The file argument is " + seq_File)

motif_File = sys.argv[2]
print("The file argument is " + motif_File)

# Open the muilti-fasta file
dnaSequence = open(seq_File)
dnaMotif = open(motif_File)

# Loop through dnaMotif file and store in String.
lines_dnaMotif = dnaMotif.readlines()
motifStr = ""

for lined_dnaMotif in lines_dnaMotif:
	for charMotif in lined_dnaMotif:
		motifStr = motifStr+charMotif
		#print(motifStr)
	#print("", end = "")

motifStr = motifStr.rstrip('\n')

# Loop through dnaSequence file and store to string.
# to parse the muilti-fasta file inside a loop to go through gene name text file
lines_dnaSeq = dnaSequence.readlines()
dnaSeqStr = ""

for lined_dnaSeq in lines_dnaSeq:
	for charSeq in lined_dnaSeq:
		dnaSeqStr = dnaSeqStr+charSeq
		#print(dnaSeqStr)
	#print("", end = "")

#dnaSeqStr = dnaSeqStr.rstrip("\n")

# .find() motifStr in dnaSeqStr
countMotifFound = 0
motifLength = len(motifStr)
seqLength = len(dnaSeqStr)

found = []
index = 0
indexEnd = motifLength
y = 0


while index < seqLength:
	indexEnd = index + motifLength
	x = dnaSeqStr.find(motifStr, index, indexEnd)
	print("The index is {0} and the indexEnd is {1}".format(index, indexEnd))
	if x > y:
		countMotifFound += 1
		found.append(x+1)
		print(x)
	index += 1

print("There are {0} motifs at {1}".format(countMotifFound, index))
print(found)
# Close files to end program
dnaSequence.close()
dnaMotif.close()