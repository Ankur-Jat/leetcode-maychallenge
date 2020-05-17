"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.
"""
class Solution(object):
    def isPerfectSquare(self, num):
        """
        Yet to do
        :type num: int
        :rtype: bool
        """

def test():
    testCases = [
        {
            "input": 16,
            "output": True
        },
        {
            "input": 14,
            "output": False
        },
    ]
    for testCase in testCases:
        expected = testCase["output"]
        result = Solution().isPerfectSquare(testCase["input"])
        assert expected == result, "Expected: {0} Got: {1}".format(expected, result)

if __name__ == "__main__":
    test()