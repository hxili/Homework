# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list

import random
import sys
n = 1000000
count = 0
calendar = [i+1 for i in range(int(sys.argv[1]))]
for i in range(n):
	birthdays = []
	share_birthday = 0
	for j in range(int(sys.argv[2])):
		birthday = random.choice(calendar)
		try:
			birthdays.index(birthday)
			share_birthday += 1
			break
		except:
			birthdays.append(birthday)
	if share_birthday != 0: count += 1
print(f'{count/n:.3f}')

"""
python3 33birthday.py 365 23
0.571
"""
