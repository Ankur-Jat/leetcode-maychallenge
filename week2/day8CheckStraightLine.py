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
        slopFound = False
        for coordinate in coordinates[1:]:
            try:
                slop = ((coordinates[0][1] - coordinate[1]) * 1.0) / (coordinates[0][0] - coordinate[0])   
                slopFound = True
                break
            except ZeroDivisionError:
                pass
        for coordinate in coordinates[1:]:
            if slopFound == False:
                if coordinate[0] != coordinates[0][0]:
                    # print("In X case", coordinate)
                    allAreInLine = False
                    break
            else:
                new_y = slop * (coordinate[0] - coordinates[0][0]) + coordinates[0][1]
                if new_y != coordinate[1]:
                    # print("In y case", coordinate, slop)
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
        {
            "input": [[0,0],[0,1],[0,-1]],
            "output": True
        },
        {
            "input": [[2,1],[4,2],[6,3]],
            "output": True
        }
    ]
    for testCase in testCases:
        expected = testCase["output"]
        result = Solution().checkStraightLine(testCase["input"])
        assert expected == result, "FAILED!: for Input: {} Expected: {} Got: {}"\
            .format(testCase["input"], expected, result)

if __name__ == "__main__":
    test()