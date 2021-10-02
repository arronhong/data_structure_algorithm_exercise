from typing import List


def maximum_subarray(nums: List[int]) -> int:
    ret = float('-inf')
    extend_max = 0
    for n in nums:
        extend_max += n
        ret = max(ret, extend_max)
        if extend_max < 0:
            extend_max = 0

    return ret


if __name__ == '__main__':
    assert 6 == maximum_subarray([-2,1,-3,4,-1,2,1,-5,4])
    assert 1 == maximum_subarray([1])
    assert 23 == maximum_subarray([5,4,-1,7,8])
    assert -1 == maximum_subarray([-2, -3, -1, -5])
