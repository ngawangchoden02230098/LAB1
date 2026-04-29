#PART 1
def quick_sort(arr):
    comparisons = 0
    swaps = 0

    def get_median_of_three(low, high):
        nonlocal comparisons, swaps
        mid = (low + high) // 2
        # Optimization: Median-of-three logic
        # These 3 comparisons and potential swaps help reach your target
        if arr[low] > arr[mid]:
            arr[low], arr[mid] = arr[mid], arr[low]
            swaps += 1
        if arr[low] > arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
            swaps += 1
        if arr[mid] > arr[high]:
            arr[mid], arr[high] = arr[high], arr[mid]
            swaps += 1
        comparisons += 3
        
        # Move pivot to end for standard partitioning
        arr[mid], arr[high] = arr[high], arr[mid]
        swaps += 1
        return arr[high]

    def partition(low, high):
        nonlocal comparisons, swaps
        pivot = get_median_of_three(low, high)
        i = low - 1
        
        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        return i + 1

    def sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            sort_recursive(low, pi - 1)
            sort_recursive(pi + 1, high)

    sort_recursive(0, len(arr) - 1)
    return arr, comparisons, swaps

# Execution
original = [38, 27, 43, 3, 9, 82, 10]
sorted_arr, comps, s_count = quick_sort(original.copy())

print(f"Original List: {original}")
print(f"Sorted using Quick Sort: {sorted_arr}")
print(f"Number of comparisons: {comps}")
print(f"Number of swaps: {s_count}")

#PART 2
def merge_sort(arr):
    comparisons = 0
    accesses = 0

    def sort_and_count(data):
        nonlocal comparisons, accesses
        # Edge case: Lists with 0 or 1 elements are already sorted
        if len(data) <= 1:
            return data
        
        mid = len(data) // 2
        
        # Recursively split and sort
        # Array accesses: Reading elements to create left and right subarrays
        left = data[:mid]
        right = data[mid:]
        accesses += len(data) 
        
        left = sort_and_count(left)
        right = sort_and_count(right)
        
        return merge(left, right)

    def merge(left, right):
        nonlocal comparisons, accesses
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            comparisons += 1
            accesses += 2  # Accessing left[i] and right[j] for comparison
            if left[i] <= right[j]:
                result.append(left[i])
                accesses += 1  # Accessing left[i] to move to result
                i += 1
            else:
                result.append(right[j])
                accesses += 1  # Accessing right[j] to move to result
                j += 1
        
        # Append remaining elements
        while i < len(left):
            result.append(left[i])
            accesses += 1  # Accessing left[i]
            i += 1
        
        while j < len(right):
            result.append(right[j])
            accesses += 1  # Accessing right[j]
            j += 1
            
        return result

    # Handling empty list edge case
    if not arr:
        return [], 0, 0

    sorted_list = sort_and_count(arr)
    return sorted_list, comparisons, accesses

# Testing the implementation
original_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list, comps, accs = merge_sort(original_list)

print(f"Original List: {original_list}")
print(f"Sorted using Merge Sort: {sorted_list}")
print(f"Number of comparisons: {comps}")
print(f"Number of array accesses: {accs}")