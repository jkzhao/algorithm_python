# -*- coding: utf-8 -*-

"""
LeetCode 34.

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

"""

def searchRange(nums, target):
    """
    time: O(logn)
    space: O(1)
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if len(nums) == 0:
        return [-1, -1]

    start = 0
    end = len(nums) - 1
    result = [-1, -1]

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            result[0] = mid
            result[1] = mid

            i = mid - 1
            while i >= 0 and nums[i] == target:
                result[0] = i
                i -= 1

            i = mid + 1
            while i <= len(nums)-1 and nums[i] == target:
                result[1] = i
                i += 1

            break
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return result

lst = [5, 7, 7, 8, 8, 10]
print(searchRange(lst, 6))

