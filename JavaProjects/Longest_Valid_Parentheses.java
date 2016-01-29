// QESTION: LEETCODE
// PROGRAM AUTHOR: TIANZHI CHEN

// Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
// For "(()", the longest valid parentheses substring is "()", which has length = 2.
// Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

from heapq import *
import bisect

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = ')' + s
        count = 0
        mx = 0
        h = {}
        for indx, c in enumerate(s):
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            h[count] = h.get(count, [])
            i = bisect.bisect_left(h[count], indx)
            h[count].insert(i,indx)

            check = count - 1
            if h.get(check):
                for j in range(len(h[count])):
                    if indx - h[count][j] > mx:
                        if h[count][j] > h.get(check)[-1]:
                            mx = max(indx - h[count][j], mx)
                            break
                    else:
                        break
            else:
                mx = max(indx - h[count][0] , mx)
        return mx
