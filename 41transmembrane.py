# 41transmembrane.py

# Write a program that predicts which proteins in a proteome are transmembrane

# Transmembrane proteins are characterized by having
#    1. a hydrophobic signal peptide near the N-terminus
#    2. other hydrophobic regions to cross the plasma membrane

# Both the signal peptide and the transmembrane domains are alpha-helices
# Therefore, they do not contain Proline

# Hydrophobicity can be measured by Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot

# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# Hint: copy mcb185.py to your homework repo and import that
# Hint: create a function for KD calculation
# Hint: create a function for hydrophobic alpha-helix
# Hint: use the same function for both signal peptide and transmembrane
import mcb185
import sys
aas = 'IVLFCMAGTSWYPHEQDNKR'
kd = (4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.3, -1.6, -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5)

#get the KD value for each aa in the protein
def KD(seq):
	seqkd = len(seq) * [0]
	for i in range(len(aas)):
		aa = aas[i]
		position = 0
		for j in range(seq.count(aa)):
			if seq.count(aa) == 0:
				continue
			else:
				position += seq[position:].find(aa)
				seqkd[position] = kd[i]
				position += 1
	return seqkd

#calculate the average KD value of peptide and judge it	
def hydro(seqkd, domain, length, s):
	sKD = 0
	win = seqkd[:length]
	for each in win:
		sKD += each
	for i in range(domain-length):
		if sKD/length > s and -1.6 not in win: 
			return True
		else:
			sKD = sKD - seqkd[i] + seqkd[i + length]
			win = win[1:] + [seqkd[i+length]]


for name, seq in mcb185.read_fasta(sys.argv[1]):
	try: 
		if hydro(KD(seq), 30, 8, 2.5) and hydro(KD(seq[::-1]), len(seq)-30, 11, 2.0): print(name)
	except:
		continue

"""
python3 41transmembrane.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str. K-12 substr. MG1655]
NP_414568.1 lipoprotein signal peptidase [Escherichia coli str. K-12 substr. MG1655]
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Escherichia coli str. K-12 substr. MG1655]
NP_414607.1 DedA family protein YabI [Escherichia coli str. K-12 substr. MG1655]
NP_414609.1 thiamine ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr. MG1655]
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia coli str. K-12 substr. MG1655]
NP_414695.1 iron(III) hydroxamate ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414699.1 PF03458 family protein YadS [Escherichia coli str. K-12 substr. MG1655]
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str. K-12 substr. MG1655]
...
"""
