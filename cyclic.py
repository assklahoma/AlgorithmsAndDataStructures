print("Cyclic Structures")

while True:
    n = int(input("Enter a two-digit number (N): "))
    if 10 <= abs(n) <= 99:
        break
    print("Invalid input. Please enter a valid two-digit number.")

i = 1
total_sum = 0

while i <= n:
    if i % 3 == 0:
        total_sum += i
    i += 1

print(f"The final sum of the series (S) = {total_sum}")
