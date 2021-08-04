import math
from copy import copy


def left_child(i):
    return i * 2 + 1


def right_child(i):
    return i * 2 + 2


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def max_heapify(arr: list, node_idx: int, heap_size: int = None):
    """
    When it is called, MAX-HEAPIFY assumes that the binary trees rooted at
    LEFT(i) and RIGHT(i) are maxheaps
    """
    heap_size = heap_size or len(arr)

    largest = node_idx
    l = left_child(node_idx)
    r = right_child(node_idx)
    if l < heap_size and arr[l] > arr[largest]:
        largest = l
    if r < heap_size and arr[r] > arr[largest]:
        largest = r
    if largest != node_idx:
        swap(arr, largest, node_idx)
        max_heapify(arr, largest, heap_size)


def build_max_heap(arr: list):
    last_non_leaf_node = math.floor((len(arr)-1)/2)
    for i in range(last_non_leaf_node, -1, -1):
        max_heapify(arr, i)


def iterative_max_heapify(arr, node_idx, heap_size = None):
    heap_size = heap_size or len(arr)
    while True:
        largest = node_idx
        l = left_child(node_idx)
        r = right_child(node_idx)
        if l < heap_size and arr[l] > arr[largest]:
            largest = l
        if r < heap_size and arr[r] > arr[largest]:
            largest = r
        if largest != node_idx:
            swap(arr, largest, node_idx)
            node_idx = largest
            continue
        else:
            break


def heap_sort(arr: list):
    if len(arr) <= 1:
        return arr

    build_max_heap(arr)
    heap_size = len(arr)
    while heap_size > 2:
        swap(arr, 0, heap_size-1)
        heap_size -= 1
        max_heapify(arr, 0, heap_size)

    swap(arr, 0, 1)


if __name__ == '__main__':
    test_cases = [
        ([27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0],
         ([27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0], 2)),
        ([27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0],
         ([27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0], 9)),
    ]
    for expected, (A, I) in test_cases:
        input = copy(A)
        max_heapify(A, I)
        assert expected == A, \
            f'max_heapify fail, {expected=}, {input=}, {I=}, actual={A}'

    test_cases = [
        ([27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0],
         ([27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0], 2)),
        ([27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0],
         ([27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0], 9)),
    ]
    for expected, (A, I) in test_cases:
        input = copy(A)
        iterative_max_heapify(A, I)
        assert expected == A, \
            f'iterative_max_heapify fail, {expected=}, {input=}, {I=}, actual={A}'

    test_cases = [
        ([84, 22, 19, 10, 3, 17, 6, 5, 9], [5, 3, 17, 10, 84, 19, 6, 22, 9]),
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
    ]
    for expected, A in test_cases:
        input = copy(A)
        build_max_heap(A)
        assert expected == A, \
            f'build_max_heap fail, {expected=}, {input=}, actual={A}'

    test_cases = [
        [5, 13, 2, 25, 7, 17, 20, 8, 4],
        [],
        [1],
        [2, 1],
    ]
    for tc in test_cases:
        input = copy(tc)
        expected = sorted(input)
        heap_sort(tc)
        assert expected == tc, \
            f'heap_sort fail, {expected=}, {input=}, actual={tc}'
