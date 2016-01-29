# QESTION: LEETCODE
# PROGRAM AUTHOR: TIANZHI CHEN
# Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits. You should try to optimize your time and space complexity.
#
# Example 1:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# return [9, 8, 6, 5, 3]
#
# Example 2:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# return [6, 7, 6, 0, 4]
#
# Example 3:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# return [9, 8, 9]

class Solution(object):

    def maxNumber(self, nums1, nums2, k):
        def prep(nums, k):
            drop = len(nums) - k
            out = []

            for n in nums:
                while out and drop and out[-1] < n:
                    drop -= 1
                    out.pop()

                out.append(n)
            return out[:k]

        def merge(num1,num2):
            return [max(num1,num2).pop(0) for _ in num1 + num2]

        return max(merge(prep(nums1, i), prep(nums2, k - i)) for i in range(k + 1) if i <= len(nums1) and k - i <= len(nums2))
