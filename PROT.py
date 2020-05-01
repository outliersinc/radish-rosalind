#! usr/bin/env python3.7

import sys

# PROT Program involves the Translation of RNA to Protein Python3.7 Script that takes a file from command line arguments
#  Than Prints the output to Standard Out.

# Written by Marcus W. on April 30, 2020

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
	rna_File = sys.argv[1]
	rnaSequence = open(rna_File)
	print("The file is " + rnaSequence)
except:
	rnaSeq = open('test.txt', 'r')

# Initialize variables
protein = " "
aa = " "
dict = {'UUU': 'F',
		'UUC': 'F',
		'UUA': 'L',
		'UUG': 'L',
		'UCU': 'S',
		'UCC': 'S',
		'UCA': 'S',
		'UCG': 'S',
		'UAU': 'Y',
		'UAC': 'Y',
		'UAA': 'Stop',
		'UAG': 'Stop',
		'UGU': 'C',
		'UGC': 'C',
		'UGA': 'Stop',
		'UGG': 'W',
		'CUU': 'L',
		'CUC': 'L',
		'CUA': 'L',
		'CUG': 'L',
		'CCU': 'P',
		'CCC': 'P',
		'CCA': 'P',
		'CCG': 'P',
		'CAU': 'H',
		'CAC': 'H',
		'CAA': 'Q',
		'CAG': 'Q',
		'CGU': 'R',
		'CGC': 'R',
		'CGA': 'R',
		'CGG': 'R',
		'AUU': 'I',
		'AUC': 'I',
		'AUA': 'I',
		'AUG': 'M',
		'ACU': 'T',
		'ACC': 'T',
		'ACA': 'T',
		'ACG': 'T',
		'AAU': 'N',
		'AAC': 'N',
		'AAA': 'K',
		'AAG': 'K',
		'AGU': 'S',
		'AGC': 'S',
		'AGA': 'R',
		'AGG': 'R',
		'GUU': 'V',
		'GUC': 'V',
		'GUA': 'V',
		'GUG': 'V',
		'GCU': 'A',
		'GCC': 'A',
		'GCA': 'A',
		'GCG': 'A',
		'GAU': 'D',
		'GAC': 'D',
		'GAA': 'E',
		'GAG': 'E',
		'GGU': 'G',
		'GGC': 'G',
		'GGA': 'G',
		'GGG': 'G' }

# Loop to parse the RNA Sequence inside a loop to go through gene name text file
for lines in rnaSequence:
	for char in range(0,len(lines)-1, 3):
		codon = lines[char] + lines[char+1] + lines[char+2]
		print("The current codon is: " + codon)
		aa = dict[codon]
		if aa == 'Stop':
			pass
		else:
			protein += aa

print("The protein is " + protein)
# Close files to end program
rnaSequence.close()