# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'
GC = 0
for i in dna:
	if i == 'C' or i == 'G': GC += 1
print(f'{GC/len(dna):.2f}')

"""
python3 24gc.py
0.42
"""
