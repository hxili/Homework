# 61kmers.py

# Make a program that reports the kmer counts for a fasta file
# Your program should take 2 arguments:
#    1. The file name
#    2. The size of k

# Hint: use argparse
# Hint: use mcb185.read_fasta()
import mcb185
import argparse

parser = argparse.ArgumentParser(description='Brief description of program.')
parser.add_argument('file', metavar='<path>', type=str, help='the file name')
parser.add_argument('size', metavar='<int>', type=int, help='the size of k')
arg = parser.parse_args()

kmers = {}
for name, seq in mcb185.read_fasta(arg.file):
	for i in range(len(seq)-arg.size+1):
		kmer = seq[i:i+arg.size]
		if kmer not in kmers: kmers[kmer] = 0
		kmers[kmer] += 1

for kmer, count in kmers.items(): print(kmer, count)




"""
python3 60kmers.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 2
AA 338006
AC 256773
AG 238013
AT 309950
CA 325327
CC 271821
CG 346793
CT 236149
GA 267384
GC 384102
GG 270252
GT 255699
TA 212024
TC 267395
TG 322379
TT 339584
"""
