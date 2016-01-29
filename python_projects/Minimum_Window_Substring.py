#  QESTION: LEETCODE
#  PROGRAM AUTHOR: TIANZHI CHEN
#  Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
#
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".
#
# Note:
# If there is no such window in S that covers all characters in T, return the empty string "".
#
# If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.


class Solution(object):
    def enough(self, target, what_we_have):

        for k in target:
            if target[k] > what_we_have.get(k,0):
                return False

        return True

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Assume all capital
        rt = s[:]
        h = {}
        h2 = {}
        for i in t:
            h[i] = h.get(i,0)
            h[i] += 1

        start = 0
        end = 0

        found = False
        while end < len(s):
            h2[s[end]] = h2.get(s[end], 0)
            h2[s[end]] += 1
            while self.enough(h,h2):
                found = True
                if end - start + 1 < len(rt):
                    rt = s[start:end+1]

                h2[s[start]] = h2.get(s[start], 0)
                h2[s[start]] -= 1
                start += 1
            end += 1
        if found:
            return rt
        else:
            return ""
