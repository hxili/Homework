#!/usr/bin/env python3
# 50dust.py

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. the entropy of each window is centered (N's in the middle of windows)
# 2. has option and default value for window size
# 3. has option and default value for entropy threshold
# 4. has a switch for N-based or lowercase (soft) masking
# 5. works with uppercase or lowercase input files
# 6. works as an executable

# Optional: make the algorithm faster (see 29gcwin.py for inspiration)
# Optional: benchmark your programs with different window sizes using time

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)

import argparse
import mcb185
import math

parser = argparse.ArgumentParser(description='Brief description of program.')
parser.add_argument('-w', metavar='<int>', type=int, help='window size', default = 11)
parser.add_argument('-t', metavar='<float>', type=float, help='entropy threshold', default = 1.4)
parser.add_argument('-s', action='store_true', help='on/off switch for N-based/lowercase masking')
parser.add_argument('file', type=str, metavar='<path>', help='some file')
arg = parser.parse_args()
c = 'ACGT'
m = arg.w // 2

if arg.s == True:
	def convert(nucleotide):
		return nucleotide.lower()
else:
	def convert(nucleotide):
		return 'N'


for name, seq in mcb185.read_fasta(arg.file):
	seql = list(seq.upper())
	win = seq[:arg.w]
	H = [0] * len(c)
	p = [0] * len(c)
	count = [0] * len(c)
	seqout = ''
	
#Calculate the entropy of the first window
	for i in range(len(c)):
		count[i] = win.count(c[i])
		p[i] = count[i] / arg.w
		if p[i] != 0:
			H[i] -= p[i] * math.log2(p[i])
			
#Move the window and replace the nucleotide in the middle of window whose entropy is lower than threshold
	for i in range(len(seq)-arg.w):
		if sum(H) < arg.t:
			seql[i+m] = convert(seql[i+m])
		ps = c.find(win[0])
		count[ps] -= 1
		p[ps] = count[ps] / arg.w
		win = win[1:] + seq[i+arg.w]
		pe = c.find(win[-1])
		count[pe] += 1
		p[pe] = count[pe] / arg.w
		for i in range(2):
			if p[ps] != 0: H[ps] = -p[ps] * math.log2(p[ps])
			else:         H[ps] = 0
			ps = pe

#Output results
	for i in range(len(seq) // 60):
		seqout += ''.join(seql[:60]) + '\n'
		seql = seql[60:]
	seqout += ''.join(seql)
	print(f">{name}", seqout, sep = '\n')


"""
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGCTTTTcATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTaaaaaaaGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAattaaaattttATTGACTTAGG
TCACTAAATacTTTAACCAATATAGGCATAGCGCACAGACAGAtAaaaaTTACAGAGTAC
ACAacATCCATGAAACGCATTAGCACCACCATTACCAccaccatCACCATTACCACAGGT
AACGGTGCgGGCTGACGCGTACAGGAAACacagaaaaAAGCCCGCACCTGACAGTGCGGG
CTttttttTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AGGCAGggGCaGGTGGCCACCGTCcTCtctgcccCcgcCAAAatcaccaacCACCTGGTG
GCGATGATTGaAAAAacCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA

Timings
win alg1 alg2
11  28.7 25.8
25  30.4 26.1
100 33.2 26.1
200 37.4 25.9
"""
