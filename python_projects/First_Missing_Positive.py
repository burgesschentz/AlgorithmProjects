 # QESTION: LEETCODE
 # PROGRAM AUTHOR: TIANZHI CHEN
 
# Given an unsorted integer array, find the first missing positive integer.
#
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
#
# Your algorithm should run in O(n) time and uses constant space.

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            while nums[i] > 0 and nums[i] != i + 1 and nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                self.swap(nums, i, nums[i]-1)
            i += 1
        for j,n in enumerate(nums):
            if n != j + 1:
                return j + 1
        return len(nums) + 1
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        return
