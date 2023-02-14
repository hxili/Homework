# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below
import random
import sys
genome_size = int(sys.argv[1])
read_num = int(sys.argv[2])
read_len = int(sys.argv[3])
genome = genome_size * [0]
for i in range(read_num):
	start = random.randint(0, genome_size - read_len)
	for j in range(read_len):
		genome[j + start] += 1
print(min(genome[read_len:-read_len]), max(genome[read_len:-read_len]), 
f'{sum(genome[read_len:-read_len]) / (genome_size - 2 * read_len):.5f}')

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
