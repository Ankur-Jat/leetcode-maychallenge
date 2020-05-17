"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
"""
from collections import OrderedDict
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        charCountDict = OrderedDict()
        counter = 0
        for char in s:
            dictValue = charCountDict.get(char)
            if dictValue:
                dictValue[1] += 1
            else:
                charCountDict[char] = [counter, 1]
            counter += 1
        for key in charCountDict.keys():
            if charCountDict[key][1] == 1:
                return charCountDict[key][0]
        return -1

def test():
    testCases = [
        {
            "input": "leetcode",
            "output": 0
        },
        {
            "input": "loveleetcode",
            "output": 2
        },
    ]
    for testCase in testCases:
        expected = testCase["output"]
        result = Solution().firstUniqChar(testCase["input"])
        assert expected == result, "Expected: {0} Got: {1}".format(expected, result)

if __name__ == "__main__":
    test()
        