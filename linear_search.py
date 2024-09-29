def linear_search(arr, target):
    """
    Returns the index of the target if it exists, else returns None
    """
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target found at index", index)
    else:
        print("Target not found in arr")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 4)
verify(result)
