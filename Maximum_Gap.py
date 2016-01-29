 # QESTION: LEETCODE
 # PROGRAM AUTHOR: TIANZHI CHEN
 
# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
#
# Try to solve it in linear time/space.
#
# Return 0 if the array contains less than 2 elements.
#
# You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = 0
        for num in nums:
            if num > max_num:
                max_num = num
        lst = [0] * (max_num + 1)
        for num in nums:
            lst[num] += 1
            if lst[num] == 2:
                return 0
        gap = 0
        largest_gap = 0
        for num in lst:
            if num == 0:
                gap +=1
            else:
                if gap > largest_gap:
                    largest_gap = gap
                gap = 0
        return largest_gap
