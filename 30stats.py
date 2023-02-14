# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys
import sys
print(sys.argv)
vals = []
for thing in sys.argv[1:]:
	vals.append(float(thing))
vals.sort()
Count = len(vals)
Min = min(vals)
Max = max(vals)
Mean = sum(vals) / Count
Mid = Count // 2
Sum_squares = 0
for val in vals:
	Sum_squares += (val - Mean) ** 2
Std_dev = (Sum_squares / Count) ** 0.5
if Count % 2 == 0: Mid = (vals[Mid-1] + val[Mid]) / 2
else: Mid = vals[Mid]
print(f"Count: {Count}", f"Minimum: {Min}", f"Maximum: {Max}",f"Mean: {Mean:.3f}", f"Std. dev: {Std_dev:.3f}", f"Median {Mid:.3f}", sep = "\n")




"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
