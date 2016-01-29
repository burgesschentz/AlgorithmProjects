 # QESTION: LEETCODE
 # PROGRAM AUTHOR: TIANZHI CHEN

# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
#
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Therefore, return the max sliding window as [3,3,5,5,6,7].
#
# Note:
# You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if len(nums) == 0 or k == 0:
            return []
        rt = []


        max_num = nums[0]
        min_num = nums[0]

        for n in nums:
            if n > max_num:
                max_num = n
            if n < min_num:
                min_num = n

        counts_pos = [0] * (max_num + 1)
        counts_neg = [0] * (-min_num + 1)
        for i in range(k):
            if nums[i] >= 0:
                counts_pos[nums[i]] += 1
            else:
                counts_neg[-nums[i]] += 1


        found = False


        for i in range(len(counts_pos))[::-1]:
            if counts_pos[i]!= 0:
                mx = i
                found = True
                break

        if not found:
            for i in range(len(counts_neg)):
                if counts_neg[i] != 0:
                    mx = - i
                    found = True
                    break
        if found:
            rt.append(mx)

            for i in range(k, len(nums)):
                if nums[i] >= 0:
                    counts_pos[nums[i]] += 1
                else:
                    counts_neg[-nums[i]] += 1

                if nums[i - k] >= 0:
                    counts_pos[nums[i - k]] -= 1

                    if nums[i] >= mx:
                        mx = nums[i]
                    else:
                        if counts_pos[nums[i - k]] == 0 and nums[i - k] == mx:
                            #find next
                            found = False
                            p = nums[i - k]
                            while p >= 0:

                                if counts_pos[p] != 0:
                                    mx = p
                                    found = True
                                    break

                                p -= 1
                            if not found:
                                for i in range(len(counts_neg)):
                                    if counts_neg[i] != 0:
                                        mx = -i
                                        found = True
                                        break
                else:
                    counts_neg[-nums[i - k]] -= 1
                    if nums[i] >= mx:
                        mx = nums[i]
                    else:
                        if counts_neg[-nums[i - k]] == 0 and nums[i - k] == mx:
                            found = False
                            p = nums[i - k]
                            while p < len(counts_neg):
                                if counts_neg[p] != 0:
                                    mx = - p
                                    found = True
                                    break
                                p += 1

                rt.append(mx)
        return rt
