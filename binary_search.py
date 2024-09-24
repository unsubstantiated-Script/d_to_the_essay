def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            # What we're looking for
            return midpoint
        elif list[midpoint] < target:
            # Reassigning the positions
            first = midpoint + 1
        else:
            last = midpoint - 1

    # Just in case number isn't in list.
    return None


def verify(index):
    if index is not None:
        print("Target found at index", index)
    else:
        print("Target not found in list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(numbers, 11)
verify(result)