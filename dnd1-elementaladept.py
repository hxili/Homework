# dnd1-elementaladept.py

# You are a mage with the Fire Bolt spell. This does 1d10 damage, or 5.5
# points of damage on average. If you have the Elemental Adept feat, damage
# rolls of 1 become 2. How much more damage do you do on average if you are
# an Elemental Adept? Simulate by rolling dice a million times.
import random
points = 0
n = 1000000
for i in range(n):
	a = random.randint(1, 10)
	if a == 1: points += 2
	else: points += a
print(points/n - 5.5)

"""
python3 dnd1-elementaladept.py
0.1
"""