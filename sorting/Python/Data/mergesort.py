"""Merge sort implementaion on Python."""


def merge(left, right):
    """Merge tow sorted arrays into one sorted."""
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):

        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort(array):
    """Merge sort recursively."""
    if len(array) < 2:
        return array

    middle = len(array) // 2

    return merge(merge_sort(array[:middle]), merge_sort(array[middle:]))
