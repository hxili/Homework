# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional
'''
dna = 'ACTGAAAAAAAAAAA'
rc_seq = ''
for i in dna:
    if i == 'A': r = 'T'
    elif i == 'T': r = 'A'
    elif i == 'C': r = 'G'
    else: r = 'C'
    rc_seq = r + rc_seq
print(rc_seq)
'''
# Variation: try this with the range() function and slice syntax
dna = 'ACTGAAAAAAAAAAA'
rc_seq = ''
for i in range(len(dna)):
    if dna[i] == 'A': r = 'T'
    elif dna[i] == 'T': r = 'A'
    elif dna[i] == 'C': r = 'G'
    else: r = 'C'
    rc_seq = r + rc_seq
print(rc_seq)


"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
