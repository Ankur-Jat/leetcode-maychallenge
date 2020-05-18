"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Algo: We are using a variation of Rabin-Karp.
As the strings contains only English lowercase alphabets so we will use array of length 26.
"""

class Solution(object):
    MAX_CHAR = 26

    def compareList(self, l1, l2):
        for index in range(self.MAX_CHAR):
            if l1[index] != l2[index]:
                return False
        return True

    def findAnagrams(self, string, pattern):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # Base case, if string is less than pattern
        if len(string) < len(pattern):
            return []

        patternLen = len(pattern)
        stringLen = len(string)

        patternList = [0] * self.MAX_CHAR
        subStrList = [0] * self.MAX_CHAR
        for index in range(patternLen):
            patternIndex = ord(pattern[index]) % 97
            subStrIndex = ord(string[index]) % 97
            patternList[patternIndex] += 1
            subStrList[subStrIndex] += 1
        
        startIndexOfAnagramInString = []
        for index in range(patternLen, stringLen):
            if self.compareList(patternList, subStrList):
                startIndexOfAnagramInString.append(index - patternLen)
            # Add new char 
            subStrList[ord(string[index]) % 97] += 1
            # Remove last char
            subStrList[ord(string[index - patternLen]) % 97] -= 1
        
        # Last comparision
        if self.compareList(patternList, subStrList):
            startIndexOfAnagramInString.append(stringLen - patternLen)
        return startIndexOfAnagramInString

def test():
    testCases = [
        {
            "input": {
                "string": "cbaebabacd",
                "pattern": "abc"
            },
            "output": [0, 6]
        },
        {
            "input": {
                "string": "abab",
                "pattern": "ab"
            },
            "output": [0, 1, 2]
        },
        {
            "input": {
                "string": "ab",
                "pattern": "abcd"
            },
            "output": []
        },
    ]
    for testCase in testCases:
        expected = testCase["output"]
        result = Solution().findAnagrams(testCase["input"]["string"], testCase["input"]["pattern"])
        assert expected == result, "Expected: {0} Got: {1}".format(expected, result)

if __name__ == "__main__":
    test()