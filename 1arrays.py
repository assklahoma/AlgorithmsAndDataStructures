import random

print("Practical Work #3. 1D Arrays")

# Array size definition and random generation
n = 20 
a = [random.uniform(-5, 15) for _ in range(n)]

# Output the original array, rounded to 2 decimal places for readability
print("Original array:")
print([round(val, 2) for val in a])

neg_index = -1
key = 1
index_min_mod = 0
min_mod = abs(a[0])
real_min = a[0]
total_sum = 0

# 1. Finding minimum modulo, absolute minimum, and first negative element index
i = 1
while i < n:
    if min_mod > abs(a[i]):
        min_mod = abs(a[i])
        index_min_mod = i
        
    if real_min > a[i]:
        real_min = a[i]
        
    if a[i] < 0 and key == 1:
        neg_index = i
        key = 0
        
    i += 1

# 2. Calculating sum of absolute values after the first negative element
if neg_index != -1 and neg_index < n - 1:
    i = neg_index + 1
    while i < n:
        total_sum += abs(a[i])
        i += 1

# 3. Replacing zeros with the minimum element
i = 0
while i < n:
    if a[i] == 0:
        a[i] = real_min
    i += 1

print(f"Index of the element with minimum absolute value: {index_min_mod}")
print(f"Sum of absolute values after the first negative element: {round(total_sum, 2)}")
print("Modified array:")
print([round(val, 2) for val in a])
