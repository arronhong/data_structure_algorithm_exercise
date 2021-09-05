from copy import copy


def swap(arr: list, i: int, j: int):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr: list, start: int, end: int, pivot: int) -> int:
    '''
    swap(pivot, end)
    cur pivot index = end
    while cur pivot index -1 > last index of less then val(pivot)
        if val(cur pivot index - 1) > val(cur pivot index)
            swap(cur pivot index - 1, cur pivot index)
            cur pivot index --
        else
            swap(cur pivot index - 1, last index of less then val(pivot))
            last index of less then val(pivot) ++
    '''
    swap(arr, end, pivot)
    new_pivot_idx = end
    last_lt_pivot_idx = start - 1
    while new_pivot_idx-1 > last_lt_pivot_idx:
        if arr[new_pivot_idx-1] > arr[new_pivot_idx]:
            swap(arr, new_pivot_idx-1, new_pivot_idx)
            new_pivot_idx -= 1
        else:
            last_lt_pivot_idx += 1
            swap(arr, new_pivot_idx-1, last_lt_pivot_idx)

    return new_pivot_idx


def quick_sort(arr: list):
    '''
    1. pick pivot of array
    2. partition array by pivot
    3. continue 1 and 2 until length of array is 1
    '''
    if len(arr) <= 1:
        return arr

    def _quick_sort(arr: list, start: int, end: int) -> list:
        # use end index to be pivot
        pivot = end
        new_pivot_idx = partition(arr, start, end, pivot)
        if new_pivot_idx > start + 1:
            _quick_sort(arr, start, new_pivot_idx - 1)
        if new_pivot_idx < end - 1:
            _quick_sort(arr, new_pivot_idx + 1, end)

        return arr

    return _quick_sort(arr, 0, len(arr)-1)


def simple_quick_sort(arr: list):
    if len(arr) <= 1:
        return arr

    return (simple_quick_sort([e for e in arr[1:] if e < arr[0]]) +
            [arr[0]] +
            simple_quick_sort([e for e in arr[1:] if e >= arr[0]]))


if __name__ == '__main__':
    test_cases = [
        [],
        [0],
        [-1, -2, 1, 2, 2, 3, 4],
        [4, 3, 2, 2, 1, 0, -1, -2],
        [5, 2, 5, 7, 1, 63, 67, 2, 6]
    ]
    for test_case in test_cases:
        input = copy(test_case)
        expected = sorted(test_case)
        actual = quick_sort(test_case)
        assert expected == actual, f'quick_sort fail: {input=}, {expected=}, {actual=}'

    test_cases = [
        [],
        [0],
        [-1, -2, 1, 2, 2, 3, 4],
        [4, 3, 2, 2, 1, 0, -1, -2],
        [5, 2, 5, 7, 1, 63, 67, 2, 6]
    ]
    for test_case in test_cases:
        input = copy(test_case)
        expected = sorted(test_case)
        actual = simple_quick_sort(test_case)
        assert expected == actual, f'simple_quick_sort fail: {input=}, {expected=}, {actual=}'
