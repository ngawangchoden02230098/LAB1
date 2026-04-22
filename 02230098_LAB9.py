#Task 1: Implement the Node and List Class Structure
def selection_sort(arr):
    n = len(arr)
    
    print("Original list:", arr)
    
    for i in range(n - 1):
        min_index = i
        
        # Find the index of the smallest element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
        # Print the list after each pass
        print(f"Pass {i+1}:", arr)
    
    print("Sorted list:", arr)

# Sample Input
arr = [29, 10, 14, 37, 13]
selection_sort(arr)

#Task 2: Implement basic operation
def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    print("Original list:", arr)

    for i in range(n - 1):
        min_index = i

        # Find the index of the smallest element
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap only if needed
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

        # Print after each pass
        print(f"Pass {i+1}:", arr)

    print("Sorted list:", arr)
    print("Total comparisons:", comparisons)
    print("Total swaps:", swaps)


# Sample Input
arr = [29, 10, 14, 37, 13]
selection_sort(arr)

# Task 3: Create an Index table for Indexed Search
def create_index_table(arr, block_size):
    index_table = []

    for i in range(0, len(arr), block_size):
        index_table.append((arr[i], i))

    print("Index table created:")
    for value, index in index_table:
        print(f"{value} -> {index}")

    return index_table


# Sample Input
arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
block_size = 3

index_table = create_index_table(arr, block_size)

#Task 4:  Implement Indexed Search
def indexed_search(arr, index_table, key):
    print("\nSearch key:", key)

    imin = 0
    imax = 0

    # Step 1: Find range using index table
    for i in range(len(index_table)):
        if i == len(index_table) - 1 or key < index_table[i + 1][0]:
            imin = index_table[i][1]
            if i == len(index_table) - 1:
                imax = len(arr) - 1
            else:
                imax = index_table[i + 1][1] - 1
            print("Index range found:")
            if i != len(index_table) - 1:
                print(f"{index_table[i][0]} <= {key} < {index_table[i+1][0]}")
            break

    # Step 2: Sequential search in range
    print(f"Searching from index {imin} to index {imax}:")

    for i in range(imin, imax + 1):
        print(f"Checking index {i}: {arr[i]}")
        if arr[i] == key:
            print(f"{key} found at index {i}")
            return i

    print(f"{key} not found")
    return -1

# Sample Run
key = 45
indexed_search(arr, index_table, key)

# Task 5: Test Indexed Search for a Key Not Found
key = 43
indexed_search(arr, index_table, key)