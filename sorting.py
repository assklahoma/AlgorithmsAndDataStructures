import random

print("Sorting Algorithms")

def cocktail_sort(arr):
    # Using a copy so we don't modify the original array
    a = arr.copy()
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    
    while swapped:
        swapped = False
        
        # Forward pass
        for i in range(start, end):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
                
        if not swapped:
            break
            
        swapped = False
        end -= 1
        
        # Backward pass
        for i in range(end - 1, start - 1, -1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
                
        start += 1
        
    return a

def counting_sort(arr):
    a = arr.copy()
    if not a:
        return a
        
    m = max(a)
    count = [0] * (m + 1)
    output = [0] * len(a)
    
    # Count occurrences
    for num in a:
        count[num] += 1
        
    # Cumulative sum
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        
    # Build output array
    for i in range(len(a) - 1, -1, -1):
        output[count[a[i]] - 1] = a[i]
        count[a[i]] -= 1
        
    return output

def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        
    return a

# Generating an array of 20 random elements (from 0 to 99)
original_array = [random.randint(0, 99) for _ in range(20)]

print(f"Original array: {original_array}\n")
print(f"Cocktail Sort:  {cocktail_sort(original_array)}")
print(f"Counting Sort:  {counting_sort(original_array)}")
print(f"Selection Sort: {selection_sort(original_array)}")
