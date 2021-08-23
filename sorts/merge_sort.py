from copy import copy


def merge(arr, left_start, left_end, right_end):
    left = arr[left_start:left_end+1]
    right = arr[left_end+1:right_end+1]
    i = j = 0
    k = left_start
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    if i < len(left):
        arr[k:right_end+1] = left[i:]
    else:
        arr[k:right_end+1] = right[j:]


def merge_sort(arr: list):
    def _merge_sort(arr, start, end):
        if start >= end:
            return
        mid = (end+start) // 2
        _merge_sort(arr, start, mid)
        _merge_sort(arr, mid+1, end)
        merge(arr, start, mid, end)

    if not arr:
        return arr

    _merge_sort(arr, 0, len(arr)-1)
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
        actual = merge_sort(test_case)
        assert expected == actual, f'{input=}, {expected=}, {actual=}'
