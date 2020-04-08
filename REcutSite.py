#! usr/bin/env python3.7

import sys
import fileinput

# REcutSite.py is a Python3.7 Script that takes a sequence file from command line arguments
# than created the reverse palindrome. It searches for reverse matches in size from 4 to 12 nucleotides (nt).
# Than prints the output, position and length, to Standard Out.
# This program takes a .txt file of DNA nucleotides (A,T,C,G) and converts
# The DNA sequence to the complimentary DNA sequence. (A,T,C,G).
# Remember A=T and G---C  (5' ----- 3')
#                         (3' ----- 5')
# Written by Marcus W. on April 5, 2020

# Read the read from command line.
seq_File = sys.argv[1]
print("The file argument is " + seq_File)

# Open the file into variable.
dnaSequence = open(seq_File)

# Loop through dnaSequence file and store to string.
# Parse the sequence file inside a loop to go through gene name text file.
lines_dnaSeq = dnaSequence.readlines()
dnaSeqStr = ""

# Read the contents of the file into dnaSeqStr, char by char, instead of line by line.
for lined_dnaSeq in lines_dnaSeq:
	for charSeq in lined_dnaSeq:
		dnaSeqStr = dnaSeqStr+charSeq
		#print(dnaSeqStr)
	print("", end = " ")

print("Main Attempt RE Cut")

#Initialize Variables
seqList = []
newSeqList = []

print("In dnaSeqStr: ", end = " ")

# Take the string dnaSeqString and copy the contents into a list called seqList.
for char in dnaSeqStr:
	if(char == 'A'):
		#print('T', end = " ")
		seqList.append(char)
	elif(char == 'C'):
		#print('G', end = " ")
		seqList.append(char)
	elif(char == 'G'):
		#print('C', end = " ")
		seqList.append(char)
	elif(char == 'T'):
		#print('A', end = " ")
		seqList.append(char)
print(" ")

# Flip the contents of seqList into newseqList
newseqList = seqList[::-1]

# Print to see if the lists (seqList, newseqList) are empty.
print(seqList)

#print(reverse(seqList))
print(newseqList)

for i in newseqList:
	if (i == 'A'):
		print('T', end=" ")
	elif (i == 'C'):
		print('G', end=" ")
	elif (i == 'G'):
		print('C', end=" ")
	elif (i == 'T'):
		print('A', end=" ")
print(" ")

#print("A = {0} C = {1} G = {2} T = {3}".format(varA, varC, varG, varT))
#dnaSeqStr = dnaSeqStr.rstrip("\n")

# Close files to end program
dnaSequence.close()