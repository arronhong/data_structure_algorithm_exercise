from typing import List


# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
#
# A subarray is a contiguous part of an array.
#
# example:
#     Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#     Output: 6
#     Explanation: [4,-1,2,1] has the largest sum = 6.


def maximum_subarray(nums: List[int]) -> int:
    """
    divide array into 2 subarray array_a(A[1..mid]) and array_b(A[mid+1..n])
    conquer subarrays to find maximum subarray of the subarray recursively
    we can find out maximum subarray in one of three condition
        1. in subarray a which from 1 to mid
        2. in subarray b which from mid + 1 to n
        3. a subarray which cross mid point from i to j
           where 1 <= i <= mid < mid + 1 <= j <= n
    so compare three subarray to find out which is bigger
    time complexity: O(nlogn)
    """
    def _maximum_subarray(nums, lo, hi):
        if lo == hi:
            return nums[lo]

        mid = lo + (hi - lo) // 2
        left = _maximum_subarray(nums, lo, mid)
        right = _maximum_subarray(nums, mid + 1, hi)

        cross_left = float('-inf')
        cross_left_continue = 0
        for i in range(mid, lo - 1, -1):
            cross_left_continue += nums[i]
            cross_left = max(cross_left, cross_left_continue)

        cross_right = float('-inf')
        cross_right_continue = 0
        for i in range(mid + 1, hi + 1):
            cross_right_continue += nums[i]
            cross_right = max(cross_right, cross_right_continue)
        cross = cross_right + cross_left
        return max(left, right, cross)

    return _maximum_subarray(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    assert 6 == maximum_subarray([-2,1,-3,4,-1,2,1,-5,4])
    assert 1 == maximum_subarray([1])
    assert 23 == maximum_subarray([5,4,-1,7,8])
