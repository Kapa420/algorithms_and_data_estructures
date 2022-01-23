"""Function for the implementation of the sorting methods."""
from Data.inserctionsort import insertion_sort
from Data.mergesort import merge_sort
from Data.timsort import timsort
from Data.dynamicarray import DynamicArray
from random import randint
import time


def insertion_sort_implementation(array):
    """Implement insertion sort function."""
    begin1 = time.time()
    in_sortedarray = insertion_sort(array.getData())
    end1 = time.time()
    time_insertion = end1 - begin1
    print('insertion_sort', f'{time_insertion = }')
    return in_sortedarray


def merge_sort_implementation(array):
    """Implement merge sort function."""
    begin2 = time.time()
    merge_sortedarray = merge_sort(array.getData())
    end2 = time.time()
    time_merge = end2 - begin2
    print('merge_sort', f'{time_merge = }')
    return merge_sortedarray


def native_sort_implementation(array):
    """Implement native python sort method."""
    begin = time.time()
    nat_sortedarray = sorted(array.getData())
    end = time.time()
    time_native = end - begin
    print('Native sort', f'{time_native =}')
    return nat_sortedarray


def timsort_implementation(array):
    """Implement timsort method."""
    begin = time.time()
    timsort_sortedarray = timsort(array.getData())
    end = time.time()
    time_timsort = end - begin
    print('timsort', f'{time_timsort =}')
    return timsort_sortedarray


def constructor_array(n=None, data=None):
    """Set an array to work with."""
    unsortedarray = DynamicArray()
    if n is None and data is None:
        n = 1000
        i = 0
        while i < n:
            unsortedarray.add(randint(-100, 100))
            i += 1
    else:
        unsortedarray.m_data = data
    print('Done', '\n', unsortedarray.getData())
    return unsortedarray


def menu():
    """Generate the main menu."""
    print("Welcome", '\n'
          "1. Automatic array creation", '\n'
          "2. Manual array creation", '\n'
          "Press any other number to cancel."
          )
    try:
        choose = int(input("Choose: "))
    except ValueError:
        return
    else:
        if choose == 1:
            unsortedarray = constructor_array()
        elif choose == 2:
            n = int(input("Choose the size: "))
            value = []
            for i in range(0, n):
                print(f"Insert value at position {i}")
                tmp = int(input())
                value.append(tmp)
            unsortedarray = constructor_array(n, value)
    return unsortedarray
