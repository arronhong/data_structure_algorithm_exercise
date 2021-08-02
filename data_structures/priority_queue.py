import math


def left_child(i):
    return i * 2 + 1


def right_child(i):
    return i * 2 + 2


def parent(i):
    return math.floor((i-1)/2)


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def max_heapify(A: list, idx: int, heap_size: int = None):
    """
    When it is called, MAX-HEAPIFY assumes that the binary trees rooted at
    LEFT(i) and RIGHT(i) are maxheaps
    """
    heap_size = heap_size or len(A)

    largest = idx
    l = left_child(idx)
    r = right_child(idx)
    if l < heap_size and A[l] > A[largest]:
        largest = l
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != idx:
        swap(A, largest, idx)
        max_heapify(A, largest, heap_size)


class HeapUnderflow(Exception):
    pass


def maximum(A: list):
    if len(A) < 1:
        raise HeapUnderflow()

    return A[0]


def extract_max(A: list):
    if len(A) < 1:
        raise HeapUnderflow()

    swap(A, 0, len(A)-1)
    max = A.pop()
    max_heapify(A, 0)
    return max


def increase_key(A: list, i, key):
    if A[i] > key:
        raise ValueError('increased key should bigger then original')

    # A[i] = key
    # while i > 0 and A[i] > A[parent(i)]:
    #     swap(A, i, parent(i))
    #     i = parent(i)

    # improment: 利用類似insertion sort的概念
    while i > 0 and A[parent(i)] < key:
        A[i] = A[parent(i)]
        i = parent(i)
    A[i] = key


def insert(A: list, key):
    # assume -1 is -inf
    A.append(-1)
    increase_key(A, len(A)-1, key)



if __name__ == '__main__':
    A = [15,13,9,5,12,8,7,4,0,6,2,1]
    assert 15 == extract_max(A)
    assert [13,12,9,5,6,8,7,4,0,1,2] == A,f'extract_max fail,actual={A}'

    A = [1]
    assert 1 == extract_max(A)
    assert [] == A, f'extract_max fail, actual={A}'

    A = [15,13,9,5,12,8,7,4,0,6,2,1]
    insert(A, 10)
    assert [15,13,10,5,12,9,7,4,0,6,2,1,8] == A, f'insert fail, actual={A}'
