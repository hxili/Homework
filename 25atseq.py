# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers
import random
seq = ''
AT_count = 0
for i in range(30):
    if random.random() <= 0.6: 
        seq += random.choice('AT')
        AT_count += 1
    else: seq += random.choice('CG')
print(len(seq), AT_count/len(seq), seq)
"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
