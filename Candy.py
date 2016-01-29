# QESTION: LEETCODE
# PROGRAM AUTHOR: TIANZHI CHEN

# There are N children standing in a line. Each child is assigned a rating value.
#
# You are giving candies to these children subjected to the following requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?



class Solution(object):

    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        rt = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                rt[i] = rt[i-1] + 1

        for i in range(len(ratings) - 1)[::-1]:
            if ratings[i] > ratings[i+1]:
                rt[i] = max(rt[i], rt[i+1] + 1)
        return sum(rt)
