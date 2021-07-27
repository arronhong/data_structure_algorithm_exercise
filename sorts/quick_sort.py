from typing import List
from copy import copy


def partition(arr: list, idx_of_pivot: int) -> (list, list):
    lt = []
    gte = []
    for i in range(len(arr)):
        if i == idx_of_pivot:
            continue
        if arr[i] < arr[idx_of_pivot]:
            lt.append(arr[i])
        else:
            gte.append(arr[i])

    return lt, gte


def quick_sort(l: List[int]):
    '''
    1. pick pivot of array
    2. partition array by pivot, after partition, got two arrays, the one is
    all the value of array less then value of pivot, the other one is all the
    value of array greate then equal value of pivot
    3. continue 1 then 2 until length of array is 1
    '''
    if len(l) <= 1:
        return l

    val_of_pivot = l[-1]
    lt, gte = partition(l, len(l)-1)

    ans = quick_sort(lt)
    ans.append(val_of_pivot)
    ans.extend(quick_sort(gte))
    return ans


if __name__ == '__main__':
    test_cases = [
        [],
        [0],
        [-1, -2, 1, 2, 3, 4],
        [4, 3, 2, 1, 0, -1, -2],
        [5, 2, 5, 7, 1, 63, 67, 2, 6]
    ]
    for test_case in test_cases:
        input = copy(test_case)
        expected = sorted(test_case)
        actual = quick_sort(test_case)
        assert expected == actual, f'{input=}, {expected=}, {actual=}'
