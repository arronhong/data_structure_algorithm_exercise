import math


def left_child(i):
    return i * 2 + 1


def right_child(i):
    return i * 2 + 2


def parent(i):
    return math.floor((i-1)/2)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


class HeapUnderflow(Exception):
    pass


class MaxPriorityQueue:
    def __init__(self, arr: list):
        self._heap = arr
        self._build_heap()

    def _build_heap(self):
        last_non_leaf = math.floor((len(self._heap)-1)/2)
        for i in range(last_non_leaf, -1, -1):
            self._heapify(i)

    def _heapify(self, idx: int):
        largest = idx
        l = left_child(idx)
        r = right_child(idx)
        if l < len(self._heap) and self._heap[l] > self._heap[largest]:
            largest = l
        if r < len(self._heap) and self._heap[r] > self._heap[largest]:
            largest = r
        if largest != idx:
            swap(self._heap, largest, idx)
            self._heapify(largest)

    def is_empty(self):
        return not len(self._heap)

    def maximum(self):
        if self.is_empty():
            raise HeapUnderflow()

        return self._heap[0]

    def extract_max(self):
        if self.is_empty():
            raise HeapUnderflow('heap is empty')

        swap(self._heap, 0, len(self._heap)-1)
        maximum = self._heap.pop()
        self._heapify(0)
        return maximum

    def increase_key(self, idx, key):
        if not 0 <= idx < len(self._heap):
            raise IndexError('index out of range')
        if self._heap[idx] > key:
            raise ValueError('increased key should bigger then original')

        while idx > 0 and self._heap[parent(idx)] < key:
            self._heap[idx] = self._heap[parent(idx)]
            idx = parent(idx)

        self._heap[idx] = key

    def insert(self, key):
        # just append a dummy value(or -inf) to creating new node then increase
        # the key
        self._heap.append(key-1)
        self.increase_key(len(self._heap)-1, key)

    def __str__(self):
        return str(self._heap)


if __name__ == '__main__':
    max_priority_queue = MaxPriorityQueue([0,1,2,4,5,6,7,8,9,12,13,15])
    assert 15 == max_priority_queue.extract_max()
    assert 13 == max_priority_queue.extract_max()
    assert 12 == max_priority_queue.extract_max()

    assert 9 == max_priority_queue.maximum()
    assert 9 == max_priority_queue.maximum()

    expected = max_priority_queue._heap[:]
    val_of_3 = expected[3]
    expected = set(expected)
    expected.remove(val_of_3)
    expected.add(15)
    max_priority_queue.increase_key(3, 15)
    assert 15 == max_priority_queue.maximum()
    assert expected == set(max_priority_queue._heap)

    expected = set(max_priority_queue._heap[:])
    expected.add(20)
    max_priority_queue.insert(20)
    assert 20 == max_priority_queue.maximum()
    assert expected == set(max_priority_queue._heap)
