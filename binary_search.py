def binary_search(arr, target):
    first = 0
    last = len(arr) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if arr[midpoint] == target:
            # What we're looking for
            return midpoint
        elif arr[midpoint] < target:
            # Reassigning the positions
            first = midpoint + 1
        else:
            last = midpoint - 1

    # Just in case number isn't in arr.
    return None


def verify(index):
    if index is not None:
        print("Target found at index", index)
    else:
        print("Target not found in arr")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(numbers, 11)
verify(result)