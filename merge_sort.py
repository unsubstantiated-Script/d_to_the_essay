def merge_sort(arr):
    """
    Sorts a arr in ascending order.
    Returns a new sorted arr.

    Steps:
    Divide: find the midpoint of the arr and divide it into two subarrs
    Conquer: find the midpoint of the arr and divide it into two subarrs
    Combine: Merge the two subarrs

    k exists here because of the Python slice operation on an arr.
    Takes 0(n log n) time
    """
    if len(arr) <= 1:
        return arr

    # Divide
    left_half, right_half = split(arr)

    # Dividing again recursively
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(arr):
    """
    Divide the unsorted arr at midpoint into subarrs
    Returns two sub-arrs - left and right

    Takes overall 0(log n) time
    """

    mid = len(arr) // 2

    # These slice actions are expensive.
    left = arr[:mid]
    right = arr[mid:]


    return left, right


def merge(left, right):
    """
    Merges two arrs, sorting them in the process.
    Runs in overall 0(n) time
    """
    l = []
    i = 0  # for left
    j = 0  # for right

    # By itself, this cannot handle arrs w/ an odd number of items.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1
    return l


def verify_sorted(arr):
    n = len(arr)

    if n == 0 or n == 1:
        return True

    if arr[0] == arr[1]:
        return True

    return arr[0] < arr[1] and verify_sorted(arr[1:])


an_arr = [44, 33, 77, 44, 55, 22, 66, 77]
l = merge_sort(an_arr)
print(l)
print(verify_sorted(an_arr))
print(verify_sorted(l))
