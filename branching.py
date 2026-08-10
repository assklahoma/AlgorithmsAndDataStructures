import math

print("Branching Structures")
x = float(input("Enter the value of x: "))
m = 2.1
n = 1.9
k = 8.5
limit = abs(m + n)
# Calculate y based on the threshold
if x < limit:
    y = math.exp(math.cos(x)) + math.exp(m + n)
elif x > limit:
    temp_val = abs(math.log10(k * x) + m * n)
    y = math.log(temp_val)
else:
    y = math.sin(k * m * x) + math.sqrt(abs(n * x))

print(f"The value of y = {y}")
