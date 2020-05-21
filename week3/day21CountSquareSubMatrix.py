"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.


Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
"""
class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        maxRow = len(matrix)
        maxColumn = len(matrix[0])
        ansMatrix = [[0] * (maxColumn + 1) for _ in xrange(maxRow + 1)]
        squareCount = 0
        for row in xrange(1, maxRow + 1):
            for column in xrange(1, maxColumn + 1):
                if matrix[row -1][column -1]:
                    ansMatrix[row][column] = min(
                        ansMatrix[row -1][column],
                        ansMatrix[row -1][column -1],
                        ansMatrix[row][column -1]
                    ) + 1
                    squareCount += ansMatrix[row][column]
        return squareCount

def test():

    testCases = [
        {
            "input": [
                [0,1,1,1],
                [1,1,1,1],
                [0,1,1,1]
            ],
            "output": 15
        },
        {
            "input": [
                [1,0,1],
                [1,1,0],
                [1,1,0]
            ],
            "output": 7
        },
        {
            "input": [
                [1, 1],
                [0, 0],
                [1, 1]
            ],
            "output": 4
        }
    ]
    for testCase in testCases:
        expected = testCase["output"]
        result = Solution().countSquares(testCase["input"])
        assert expected == result, "Expected: {0} Got: {1}".format(expected, result)

if __name__ == "__main__":
    test()
