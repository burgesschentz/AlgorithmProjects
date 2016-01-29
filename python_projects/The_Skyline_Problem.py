
# QESTION: LEETCODE
# PROGRAM AUTHOR: TIANZHI CHEN

// Question Link : https://leetcode.com/problems/the-skyline-problem/
class Solution(object):

    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        skylines = []
        for each in buildings:
            skylines.append(self.convert_to_skyLine(each))
        return self.merge_skyline(skylines)

    def convert_to_skyLine(self, building):
        return [[building[0], building[2]] , [building[1], 0]]

    def merge_skyline(self, skylines):
        if len(skylines) == 1:
            return skylines[0]

        elif len(skylines) == 2:
            return self.getSkyline_r(skylines[0], skylines[1])

        elif len(skylines) > 2:
            sk1 = self.merge_skyline(skylines[:int(len(skylines)/2)])
            sk2 = self.merge_skyline(skylines[int(len(skylines)/2):])

            return self.getSkyline_r(sk1, sk2)
        else:
            return []

    def getSkyline_r(self, sky1, sky2):

        p1 = 0
        p2 = 0
        sk1_height = 0
        sk2_height = 0

        skyLine = []

        while p1 < len(sky1) or p2 < len(sky2):
            if p1 != len(sky1) and (p2 == len(sky2) or sky1[p1][0] < sky2[p2][0]):
                point = [ sky1[p1][0] , max(sky1[p1][1], sk2_height)]
                sk1_height = sky1[p1][1]

                if len(skyLine) == 0 or skyLine[-1][1] != point[1]:
                    skyLine.append(point)
                p1 += 1
            elif p2 != len(sky2) and (p1 == len(sky1) or sky2[p2][0] < sky1[p1][0]):
                point = [sky2[p2][0], max(sky2[p2][1], sk1_height)]

                sk2_height = sky2[p2][1]

                if len(skyLine) == 0 or skyLine[-1][1] != point[1]:
                    skyLine.append(point)
                p2 += 1
            else:
                sk1_height = sky1[p1][1]
                sk2_height = sky2[p2][1]
                point = [sky2[p2][0], max(sk2_height, sk1_height)]

                if len(skyLine) == 0 or skyLine[-1][1] != point[1]:
                    skyLine.append(point)
                p2 += 1
                p1 += 1
        return skyLine
