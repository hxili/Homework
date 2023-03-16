# 63canonical.py

# You probably learned that ATG is the only start codon, but is it?
# Write a program that reports the start codons from the E. coli genome
# Your program must:
#    1. read GCF_000005845.2_ASM584v2_genomic.gbff.gz at the only input
#    2. use a regex to find CDS coordinates
#    3. count how many different start codons there are

# Note: the sequence is at the end of the file
# Note: genes on the negative strand are marked complement(a..b)

# Hint: you can read a file twice, first to get the DNA, then the CDS
# Hint: check your CDS by examining the source protein
import re
import gzip
import sys

convert = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

with gzip.open(sys.argv[1], 'rt') as fp:
	start_codon_pos = {}
	start_codons = {}
	line = ''
	seq = ''
	# collect all start condons' position
	while 'ORIGIN' not in line:
		line = fp.readline()
		if re.search(' CDS ', line) != None:
			match = re.search('(\d+)\.\.(\d+)', line)
			if 'complement' not in line:
				start_codon_pos[int(match.group(1))-1] = '+'
			else:
				start_codon_pos[int(match.group(2))-1] = '-'

	# get the nucleotide sequence
	while True:
		line = fp.readline()
		if line.startswith('//'): break
		match = re.search('(\d+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+)', line)
		for i in range(2, 8):
			seq += match.group(i)
	seq = seq.upper()
	
	# count the number of each codon in both strands
	for pos, strand in start_codon_pos.items():
		if strand == '+':
			codon = seq[pos:pos+3]
			if codon not in start_codons:
				start_codons[codon] = 0
			start_codons[codon] += 1
		elif strand == '-':
			codonl = list(seq[pos-2:pos+1][::-1])
			codon = ''
			for n in codonl:
				codon += convert[n]
			if codon not in start_codons:
				start_codons[codon] = 0
			start_codons[codon] += 1
			
	for codon, count in start_codons.items():
		print(codon, count)


"""
python3 63canonical.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gbff.gz
ATG 3883
GTG 338
TTG 80
ATT 5
AGT 1
AAA 1
AGC 1
TTC 1
TAA 1
CGT 1
CTG 2
GAC 1
"""
