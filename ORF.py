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
count = 1
protein = []
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
		codon = lines[char] + lines[char+1] + lines[char+2]
		count += 1
		aa = dict[codon]
		if aa == 'Stop':
			pass
		else:
			protein += aa

print("The protein is {0} and the count is {1}".format(protein, count))

# Loop to parse the DNA Sequence inside a loop to go through gene name text file
for lines in dnaSeq:
	for char in range(0,len(lines)-1, 3):
		codon = lines[char] + lines[char+1] + lines[char+2]
		count += 1
		aa = dict[codon]
		if aa == 'Stop':
			pass
		else:
			protein += aa

print("The protein is {0} and the count is {1}".format(protein, count))
# Print the output.

# Close files to end program
