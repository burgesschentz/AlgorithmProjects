
# QESTION: LEETCODE
# PROGRAM AUTHOR: TIANZHI CHEN

# QUESTION LINK: https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        mx = 0

        for i in range(len(height)):
            if len(stack) == 0 or height[stack[-1]] < height[i]:
                stack.append(i)
            else:
                while len(stack) != 0 and height[i] < height[stack[-1]]:
                    smallest = height[stack.pop()]
                    if len(stack) == 0:
                        left_end = - 1
                    else:
                        left_end = stack[-1]
                    area = smallest * (i - left_end - 1)
                    mx = max(area, mx)
                stack.append(i)

        while(len(stack)!= 0):
            smallest = height[stack.pop()]
            if len(stack) == 0:
                left_end = - 1
            else:
                left_end = stack[-1]
            area = smallest * (len(height) - left_end - 1)
            mx = max(area, mx)

        return mx
