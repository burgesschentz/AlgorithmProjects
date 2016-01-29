# QESTION: LEETCODE
# PROGRAM AUTHOR: TIANZHI CHEN
# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        def get_slope_yoffset(p1, p2):
            if (p1.x - p2.x) != 0:
                slope = (float(p1.y) - float(p2.y)) / (float(p1.x) - float(p2.x))
                offset = slope * float(p1.x) - float(p1.y)  # should be same of use p2
            else:
                slope = 'infinity'
                offset = float(p1.x)
            return slope, offset
        if len(points) == 1:
            return 1
        h = {}
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    slp, os = get_slope_yoffset(points[i], points[j])
                    h[slp] = h.get(slp,set())
                    h[slp].add(points[i])
                    h[slp].add(points[j])
        mx = 0
        for v in h.values():
            mx = max(mx, len(v))
        return mx
