print("Cyclic Structures")

a = []

# Input loop until 0 is entered
while True:
    val = float(input("Enter a number (0 to stop): "))
    a.append(val)
    if val == 0:
        break

n = len(a)
total_sum = 0
count = 0
i = 0

# Calculating sum and count of elements less than the first element
while i < n:
    if a[i] < a[0]:
        total_sum += a[i]
        count += 1
    i += 1

# Calculating and printing the result with division by zero protection
if count > 0:
    res = total_sum / count
    print(f"Result (Average): {res}")
else:
    print("No elements less than the first element were found.")
