def merge_sort(arr):
    """Sorts an array using the merge sort algorithm.

    Args:
        arr: A list of elements to be sorted.

    Returns:
        A sorted list of elements.
    """

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    # Merge the sorted left and right subarrays.
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Add any remaining elements from the left subarray.
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Add any remaining elements from the right subarray.
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print(f"The sorted array is: {arr}")


"""Output:
The sorted array is: [3, 9, 10, 27, 38, 43, 82]"""
