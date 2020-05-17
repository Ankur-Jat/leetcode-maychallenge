# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3330/
class Solution(object):
    # Main Kadanes algo
    def kadaneSum(self, A):
        if len(A) == 0:
            return 0
        maxSumSoFar = A[0]
        maxSum = A[0]
        for num in A[1:]:
            maxSumSoFar = max(num, maxSumSoFar + num)
            maxSum = max(maxSum, maxSumSoFar)
        return maxSum

    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        maxSum = self.kadaneSum(A)
        arraySum = 0
        for index in xrange(len(A)):
            arraySum += A[index]
            A[index] = -A[index]
        arraySum += self.kadaneSum(A)
        
        if arraySum and arraySum > maxSum:
            return arraySum
        return maxSum
        
def test():
    testCases = [
        {
            "input": [-2,-3,-1],
            "output": -1
        },
        {
            "input": [3,-2,2,-3],
            "output": 3
        },
        {
            "input": [3,-1,2,-1],
            "output": 4
        },
        {
            "input": [5,-3,5],
            "output": 10
        },
        {
            "input": [1,-2,3,-2],
            "output": 3
        },
    ]
    for testCase in testCases:
        expected = testCase["output"]
        result = Solution().maxSubarraySumCircular(testCase["input"])
        assert expected == result, "Expected: {0} Got: {1}".format(expected, result)

if __name__ == "__main__":
    test()