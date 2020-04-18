""" 
Problem 1 - Two Sum

Given an array of integers, return indices of the two numbers such that 
they add up to a specific target.
"""

from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target)) # Should return [0, 1]