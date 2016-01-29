# QESTION: LEETCODE
# PROGRAM AUTHOR: TIANZHI CHEN
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.c = capacity
        self.h = {}
        self.q = []


    def get(self, key):
        """
        :rtype: int
        """
        rt = self.h.get(key)
        if rt:
            self.q.remove(key)

            self.q.append(key)

            return rt
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """

        # occupied or not
        occupied = self.h.get(key)
        if occupied:
            self.h[key] = value
            self.q.remove(key)
            self.q.append(key)
        else:
            if len(self.h.keys()) >= self.c:
                out = self.q.pop(0)
                self.h.pop(out)
            self.h[key] = value
            self.q.append(key)
