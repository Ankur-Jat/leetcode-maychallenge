# -*- coding: UTF-8 -*-
"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
Check if these points make a straight line in the XY plane.
"""
class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        :assumptions: assuming there are at least 3 coordinates
        : y − y1 = m(x − x1)
        """
        allAreInLine = True
        checkOnlyX = False
        slop = 0
        try:
            slop = (coordinates[0][1] - coordinates[1][1]) // (coordinates[0][0] - coordinates[1][0])   
        except ZeroDivisionError:
            checkOnlyX = True
        for coordinate in coordinates[2:]:
            if checkOnlyX and coordinate[0] != coordinates[0][0]:
                allAreInLine = False
                break
            else:
                new_y = slop * (coordinate[0] - coordinates[0][0]) + coordinates[0][1]
                if new_y != coordinate[1]:
                    allAreInLine = False
                    break
        return allAreInLine

def test():
    testCases = [
        {
            "input": [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]],
            "output": True
        },
        {
            "input": [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]],
            "output": False
        },
    ]
    for testCase in testCases:
        expected = testCase["output"]
        result = Solution().checkStraightLine(testCase["input"])
        assert expected == result, "Expected: {0} Got: {1}".format(expected, result)

if __name__ == "__main__":
    test()