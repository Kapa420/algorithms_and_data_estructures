min_merge = 32

def calcMinRun(n):
    r = 0
    while n >= min_merge:
        r |= n & 1
        n >>= 1
    return n + r
def timsort(array):
    n = len(array)
    min_run = calcMinRun(n)
    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))
            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1])
            array[start:start + len(merged_array)] = merged_array
        size *= 2
    return array
