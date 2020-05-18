"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
In other words, one of the first string's permutations is the substring of the second string.

Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

We will use a variation of Rabin-Karp algorithm
"""
class Solution(object):
    MAX_LEN = 26

    def compareList(self, list1, list2):
        for index in range(self.MAX_LEN):
            if list1[index] != list2[index]:
                return False
        return True

    def checkInclusion(self, pattern, string):
        """
        :type pattern: str
        :type string: str
        :rtype: bool
        """
        patternLen = len(pattern)
        stringLen = len(string)
        if stringLen < patternLen:
            return False

        patternList = [0] * self.MAX_LEN
        substrList = [0] * self.MAX_LEN
        for index in range(patternLen):
            patternIndex = ord(pattern[index]) % 97
            patternList[patternIndex] += 1
            substrIndex = ord(string[index]) % 97
            substrList[substrIndex] += 1
        
        for index in range(patternLen, stringLen):
            if self.compareList(patternList, substrList):
                return True
            # Remove char of last index
            substrList[ord(string[index - patternLen]) % 97] -= 1
            # Add char of current index
            substrList[ord(string[index]) % 97] += 1

        return self.compareList(patternList, substrList)

def test():
    testCases = [
        {
            "input": {
                "string": "eidbaooo",
                "pattern": "ba"
            },
            "output": True
        },
        {
            "input": {
                "string": "eidboaoo",
                "pattern": "ab"
            },
            "output": False
        },
        {
            "input": {
                "string": "ab",
                "pattern": "abcd"
            },
            "output": False
        },
    ]
    for testCase in testCases:
        expected = testCase["output"]
        result = Solution().checkInclusion(testCase["input"]["pattern"], testCase["input"]["string"], )
        assert expected == result, "Expected: {0} Got: {1} for input: {2}".format(expected, result, testCase["input"])

if __name__ == "__main__":
    test()        