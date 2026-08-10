print("Search Algorithms (Transposition Method)")

arr = [15, 3, 9, 12, 5, 8, 1, 24, 7, 10]
print(f"Initial array: {arr}\n")

search_stats = {}

def transposition_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            if i > 0:
                array[i], array[i - 1] = array[i - 1], array[i]
                return i - 1
            return i
    return -1

while True:
    target = int(input("Enter element to search (0 to exit): "))
    
    if target == 0:
        break
        
    if target in search_stats:
        search_stats[target] += 1
    else:
        search_stats[target] = 1
        
    index = transposition_search(arr, target)
    
    if index != -1:
        print(f"Element found! New index: {index}")
        print(f"Current array state: {arr}\n")
    else:
        print("Element not found.\n")

print("\n--- Search Statistics ---")
for element, count in search_stats.items():
    print(f"Element '{element}' was searched {count} time(s).")
