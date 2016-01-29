# QESTION: LEETCODE
# PROGRAM AUTHOR: TIANZHI CHEN

# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
#
# Examples:
# [2,3,4] , the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Design a data structure that supports the following two operations:
#
# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
# For example:
#
# add(1)
# add(2)
# findMedian() -> 1.5
# add(3)
# findMedian() -> 2


class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.lst = []


    def addNum(self, num):
        if len(self.lst) == 0:
            i = 0
        else:
            i = self.binary_find(num,0,len(self.lst) - 1)

        self.lst.insert(i,num)

    def binary_find(self, num, start, end):

        if end == start:
            if self.lst[start] > num:
                return start
            else:
                return start + 1

        if end - start == 1:
            if self.lst[start] > num:
                return start
            elif self.lst[end] > num:
                return end
            else:
                return end + 1

        h = int((end - start) / 2) + start
        if num > self.lst[h]:
            return self.binary_find(num, h + 1, end)
        elif num < self.lst[h]:
            return self.binary_find(num, start, h - 1)
        else:
            return h


    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        half = int(len(self.lst) / 2)

        if len(self.lst) % 2 == 0:
            medi = float(self.lst[half] + self.lst[half - 1] ) / 2.0

        else:
            medi = self.lst[half]

        return medi
