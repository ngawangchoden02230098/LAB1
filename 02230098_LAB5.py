# Part 1: Sequential Search Implementation
def sequential_search(arr, target):
    comparisons = 0
    
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    
    return -1, comparisons


# Example usage
arr = [23, 45, 12, 67, 89, 34, 56]
target = 67

index, comparisons = sequential_search(arr, target)

print("List:", arr)
print("Searching for", target, "using Sequential Search")

if index != -1:
    print("Found at index", index)
else:
    print("Not found")

print("Number of comparisons:", comparisons)

# Part 2: Binary search Implementation
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2

        comparisons += 1  # for equality check
        if arr[mid] == target:
            return mid, comparisons

        comparisons += 1  # for less-than check
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons

# Example usage
arr = [12, 23, 34, 45, 56, 67, 89]
target = 67
index, comparisons = binary_search(arr, target)

print("Sorted List:", arr)
print("Searching for", target, "using Binary Search")

if index != -1:
    print("Found at index", index)
else:
    print("Not found")

print("Number of comparisons:", comparisons)
    