# This program can align two sequences from command line by Smith-Waterman algorithm with a linear gap penalty
import argparse

parser = argparse.ArgumentParser(description='Brief description of program.')
parser.add_argument('--mat', metavar='<int>', type=int, help='match score', default=3)
parser.add_argument('--mis', metavar='<int>', type=int, help='mismatch score', default=-3)
parser.add_argument('--gap', '-g', metavar='<int>', type=int, help='gap score', default=2)
parser.add_argument('--seq', '-s', nargs=2, metavar='<str>', type=str, help='two sequences to be aligned')
arg = parser.parse_args()

# Generate scoring matrix and track matrix
smatrix = [[0 for i in range(len(arg.seq[0])+1)] for j in range(len(arg.seq[1])+1)]
tmatrix = [[0 for i in range(len(arg.seq[0]))] for j in range(len(arg.seq[1]))]
highest = 0 # highest score in matrix
spos = [] # stop position

for i in range(len(arg.seq[1])):
	for j in range(len(arg.seq[0])):
		if arg.seq[1][i] == arg.seq[0][j]: h = smatrix[i][j] + arg.mat
		else:                              h = smatrix[i][j] + arg.mis
		if h < 0: h = 0
		if smatrix[i][j+1] - arg.gap > h:
			h = smatrix[i][j+1] - arg.gap
			tmatrix[i][j] = 1
		if smatrix[i+1][j] - arg.gap > h:
			h = smatrix[i+1][j] - arg.gap
			tmatrix[i][j] = -1
		smatrix[i+1][j+1] = h
		
		# Get the position of highest score
		if h > highest:
			highest = h
			spos = [[i, j]]
		elif h == highest:
			spos.append([i, j])

# print the max score
print(f'the score of the maximum alignment is {highest}')
print('all possible alignments with the maximum score:')
for each in spos:
	# Traceback
	track = [each]
	while True:
		x = each[0]
		y = each[1]
		if tmatrix[x][y] == 0:
			x -= 1
			y -= 1
		elif tmatrix[x][y] == 1:
			x -= 1
		else:
			y -= 1
		if smatrix[x+1][y+1] == 0: break
		each = [x, y]
		track.append(each)
	track = track[::-1]

	# Get the position of gap in sequence
	gap = [[],[]]
	for i in range(2):
		for j in range(len(track)-1):
			if track[j+1][i] - track[j][i] == 0:
				gap[1-i].append(j+1)

	# Output
	seq = [[], []]
	for i in range(2):
		for j in range(len(track)):	
			if j in gap[i]: seq[i].append('-') 
			else:           seq[i].append(arg.seq[i][track[j][1-i]])
			
			
	for aa in seq[0]:
		print(aa, end = ' ')
	print('\t')
	for k in range(len(track)):
		if seq[0][k] == seq[1][k]: print('|', end = ' ')
		else:                      print(' ', end = ' ')   
	print('\t')
	for aa in seq[1]:
		print(aa, end = ' ')
	print('\t')
	print('\t')
