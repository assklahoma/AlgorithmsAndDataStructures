import random

print("Multidimensional Arrays")

n = 4
# Generating an n x n matrix with random integers (from -5 to 5 to ensure we get a 0)
b = [[random.randint(-5, 5) for _ in range(n)] for _ in range(n)]

print("Generated Matrix B:")
for row in b:
    print(row)

sum_odd_indices = 0
sum_abs_before_zero = 0
zero_found = False

for i in range(n):
    for j in range(n):
        # 1. Sum of elements with odd indices (flattened 1-based index calculation)
        flattened_index = i * n + j + 1
        if flattened_index % 2 != 0:
            sum_odd_indices += b[i][j]
        
        # 2. Sum of absolute values before the first zero element
        if not zero_found:
            if b[i][j] == 0:
                zero_found = True
            else:
                sum_abs_before_zero += abs(b[i][j])

print(f"Sum of elements with odd indices: {sum_odd_indices}")
print(f"Sum of absolute values before the first zero: {sum_abs_before_zero}")
