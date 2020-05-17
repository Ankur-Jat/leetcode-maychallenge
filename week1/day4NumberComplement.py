"""
Given a positive integer num, output its complement number. 
The complement strategy is to flip the bits of its binary representation.
"""
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int('0b' + ''.join(['1' if value=='0' else '0' for value in bin(num)[2:]]), 2)

def test():
    testCases = [
        {
            "input": 5,
            "output": 2
        },
        {
            "input": 1,
            "output": 0
        },
        {
            "input": 7,
            "output": 0
        },
    ]
    for testCase in testCases:
        expected = testCase["output"]
        result = Solution().findComplement(testCase["input"])
        assert expected == result, "Expected: {0} Got: {1}".format(expected, result)

if __name__ == "__main__":
    test()