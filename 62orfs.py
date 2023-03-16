# 62orfs.py

# Make a program that finds open reading frames in the E. coli genome
# Your program should read a fasta file
# There should be an optional minimum ORF size with a default value of 300 nt
# The output should be a table showing 4 columns
#     1. parent sequence identifier
#     2. begin coordinate
#     3. end coordinate
#     4. strand
#     5. first 10 amino acids of the protein

# Hint: use argparse, mcb185.read_fasta(), and mcb185.translate()
# Hint: don't use the whole genome for testing

# Note: your genes should be similar to those in the real genome
import mcb185
import argparse
import re

parser = argparse.ArgumentParser(description='Brief description of program.')
parser.add_argument('file', metavar='<path>', type=str, help='the file name')
parser.add_argument('-s', '--size', metavar='<int>', type=int, 
help='the minimum size of ORF', default=300)
arg = parser.parse_args()

#gstart_codons = ['ATG', 'GTG', 'TTG']
gstart_codons = ['ATG']
gstop_codons = ['TAA', 'TGA', 'TAG']
convert = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

# function to find specific codon
def codon_find(seq, codons):
	pos = None
	for i in range(len(seq)):
		if seq[i:i+3] not in codons:
			continue
		else:
			pos = i
			break
	return pos

# function to find orfs in given sequence
def orfs_find(seq, start_codons = gstart_codons, stop_codons = gstop_codons):
	epos_last = None
	bpos = codon_find(seq, start_codons)
	bpos_gap = bpos
	while bpos_gap != -1:
		bpos_gap = codon_find(seq[bpos+1:], start_codons)
		if bpos_gap == None: bpos_gap = -1
		if codon_find(seq[bpos:], stop_codons) == None:
			bpos += bpos_gap + 1
			continue
		epos = codon_find(seq[bpos:], stop_codons) + bpos
		if epos == None:
			bpos += bpos_gap + 1
			continue
		while (epos - bpos) % 3 != 0:
			epos_gap = codon_find(seq[epos+1:], stop_codons)
			if epos_gap == None:
				bpos += bpos_gap + 1
				break
			epos += epos_gap + 1
		else:
			if epos - bpos + 2 >= arg.size:
				if epos != epos_last:
					epos_last = epos
					yield (bpos+1, epos+3, mcb185.translate(seq[bpos:bpos+30]))
		bpos += bpos_gap + 1

# output ORFs in "+" strand
for defline, seq in mcb185.read_fasta(arg.file):
	identifier = re.search('\w+.\w', defline).group()
	for beginpos, endpos, firstseq in orfs_find(seq):
		print(identifier, beginpos, endpos, '+', firstseq)

	# get the sequence of "-" strand
	seq = seq[::-1]
	reverse_seqlist = []
	for n in seq:
		reverse_seqlist += convert[n]
	rseq = ''.join(reverse_seqlist)

	# output ORFs in "-" strand
	for beginpos, endpos, firstseq in orfs_find(rseq):
		print(identifier, len(seq)-endpos+1, len(seq)-beginpos+1, '-', firstseq)


"""
python3 62orfs.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz
NC_000913.3 108 500 - MVFSIIATRW
NC_000913.3 337 2799 + MRVLKFGGTS
NC_000913.3 2801 3733 + MVKVYAPASS
NC_000913.3 3512 4162 - MSHCRSGITG
NC_000913.3 3734 5020 + MKLYNLKDHN
NC_000913.3 3811 4119 - MVTGLSPAIW
NC_000913.3 5310 5738 - MKIPPAMANW
NC_000913.3 5683 6459 - MLILISPAKT
NC_000913.3 6529 7959 - MPDFFSFINS
NC_000913.3 7366 7773 + MKTASDCQQS
"""
