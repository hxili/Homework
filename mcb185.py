# mcb185.py

import sys
import gzip

def read_fasta(filename):

	if   filename == '-':          fp = sys.stdin
	elif filename.endswith('.gz'): fp = gzip.open(filename, 'rt')
	else:                          fp = open(filename)

	name = None
	seqs = []

	while True:
		line = fp.readline()
		if line == '': break
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				yield(name, ''.join(seqs))
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)

	yield(name, ''.join(seqs))
	fp.close()

# def other functions...

# translate function
# The standard genetic code in a dictionary
gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}


def translate(seq, frame = 0, code = gcode):

	seq = seq.upper()
	seq = seq[frame:]
	seq = seq[:((len(seq)//3)*3)]
	protein = ''
	
	for i in range(0, len(seq), 3):
		codon = seq[i:i+3]
		if codon not in code: protein += 'X'
		else:                 protein += code[codon]
	return(protein)

'''
gstart_codon = ['ATG', 'GTG', 'TTG']

def translate(seq, frame = 0, code = gcode, start_codon = gstart_codon):

	seq = seq.upper()
	seq = seq[frame:]
	seq = seq[:((len(seq)//3)*3)]
	aa_seq = ''
	scpos = []
	
	for i in range(0, len(seq), 3):
		#translate the nucleotide seq to aa seq
		codon = seq[i:i+3]
		if codon not in code: aa_seq += 'X'
		else:                 aa_seq += code[codon]
		#locate the position of start codon
		if codon in start_codon:
			scpos += [int(i/3)]
		#find the stop codon
		elif aa_seq[-1] == '*':
			if scpos != []:
				#output the longest protein
				yield(aa_seq[scpos[0]:])
				scpos = []
'''