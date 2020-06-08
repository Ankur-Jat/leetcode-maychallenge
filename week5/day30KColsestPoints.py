"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]


def testSolution():
    testCases = [
        {
            "input": {
                "K": 2,
                "points": [[3,3],[5,-1],[-2,4]]
            },
            "output": [[3,3],[-2,4]]
        },
        {
            "input": {
                "K": 1,
                "points": [[1,3],[-2,2]]
            },
            "output": [[-2,2]]
        }
    ]

    solution = Solution()
    for testCase in testCases:
        output = solution.kClosest(testCase["input"]["points"], testCase["input"]["K"])
        assert output == testCase["output"], "FAILED! Expected: {}, Got: {}".format(input["output"], output)


if __name__ == "__main__":
    testSolution()
