"""Insertion sort implementation on Python."""


def insertion_sort(m_array):
    """Implement insertion sort function."""
    if len(m_array) > 1:
        for i in range(1, len(m_array)):
            ref = m_array[i]
            j = i - 1
            while j >= 0 and ref < m_array[j]:
                m_array[j + 1] = m_array[j]
                j -= 1
                m_array[j + 1] = ref
    else:
        pass
    return m_array
