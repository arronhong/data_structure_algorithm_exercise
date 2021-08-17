from typing import List
from copy import copy


def selection_sort(arr: List):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


if __name__ == '__main__':
    test_cases = [
        [],
        [0],
        [-1, -2, 1, 2, 3, 4],
        [5, 2, 5, 7, 1, 63, 67, 2, 6]
    ]
    for test_case in test_cases:
        input = copy(test_case)
        expected = sorted(test_case)
        actual = selection_sort(test_case)
        assert expected == actual, f'{input=}, {expected=}, {actual=}'
