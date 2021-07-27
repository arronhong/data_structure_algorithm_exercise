from typing import List
from copy import copy


def insertion_sort(l: List[int]):
    if len(l) <= 1:
        return l
    for i in range(1, len(l)):
        for j in range(i-1, -1, -1):
            if l[j+1] < l[j]:
                l[j+1], l[j] = l[j], l[j+1]
                continue
            break

    return l


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
        actual = insertion_sort(test_case)
        assert expected == actual, f'{input=}, {expected=}, {actual=}'
