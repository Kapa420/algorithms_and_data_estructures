"""Implementation sorting methods on Python 3."""
from Data.implementations import insertion_sort_implementation
from Data.implementations import native_sort_implementation
from Data.implementations import merge_sort_implementation
from Data.implementations import timsort_implementation
from Data.implementations import menu


def main():
    """Define main function."""
    unsortedarray = menu()

    insertion_sort_implementation(unsortedarray)

    native_sort_implementation(unsortedarray)

    merge_sort_implementation(unsortedarray)

    print(f'sorted array = {timsort_implementation(unsortedarray)}')


if __name__ == '__main__':
    main()
