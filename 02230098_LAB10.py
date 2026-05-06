# Task 1 (Part 1: COunting sort implementation)
def counting_sort(arr):
    if not arr:
        return []

    # Find the maximum element
    max_val = max(arr)

    # Initialize count array
    count = [0] * (max_val + 1)

    # Store frequency of each element
    for num in arr:
        count[num] += 1

    # Build the sorted array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr


# Example Usage
arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr))

# Task 1 (Part 2: Part 2: Radix Sort Implementation)
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # digits 0–9

    # Count occurrences
    for i in arr:
        index = (i // exp) % 10
        count[index] += 1

    # Update count array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    return output

def radix_sort(arr):
    if not arr:
        return []

    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        arr = counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr

# Example Usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(arr))