"""
We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

Example 1:


Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
Example 2:

Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2
 

Note:

1 <= A.length <= 500
1 <= B.length <= 500
1 <= A[i], B[i] <= 2000

=> This is similar to longest common subsequence problem
"""

class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        lenA = len(A)
        lenB = len(B)
        dpMatrix = [[0] * (lenB + 1) for _ in xrange(lenA + 1)]
        for indexA in xrange(1, lenA + 1):
            for indexB in xrange(1, lenB + 1):
                if A[indexA - 1] == B[indexB - 1]:
                    dpMatrix[indexA][indexB] = 1 + dpMatrix[indexA - 1][indexB - 1]
                else:
                    dpMatrix[indexA][indexB] = max(dpMatrix[indexA - 1][indexB], dpMatrix[indexA][indexB - 1])
        return dpMatrix[-1][-1]

def test():
    testCases = [
        {
            "input": {
                "A": [1,4,2],
                "B": [1,2,4]
            },
            "output": 2
        },
        {
            "input": {
                "A": [2,5,1,2,5],
                "B": [10,5,2,1,5,2]
            },
            "output": 3
        },
        {
            "input": {
                "A": [1,1,2,1,2],
                "B": [1,3,2,3,1]
            },
            "output": 3
        },
    ]
    solution = Solution()
    for testCase in testCases:
        output = solution.maxUncrossedLines(testCase["input"]["A"], testCase["input"]["B"])
        assert output == testCase["output"], "Expected: {}, Got: {}".format(testCase["output"], output)

test()