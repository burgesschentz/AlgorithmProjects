 # QESTION: LEETCODE
 # PROGRAM AUTHOR: TIANZHI CHEN

# Given a collection of intervals, merge all overlapping intervals.
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        rt = []

        for i in sorted(intervals, key = lambda a: a.start):
            if len(rt) != 0 and rt[-1].end >= i.start:
                last = rt.pop()
                merged_interval = Interval(last.start,max(i.end, last.end))
                rt.append(merged_interval)
            else:
                rt.append(i)
        return rt
