"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have. 
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, 
so "a" is considered a different type of stone from "A"
"""
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewelDict = {}
        for char in J:
            jewelDict[char] = True
        
        jewelInStones = 0
        for char in S:
            if jewelDict.get(char):
                jewelInStones += 1
        return jewelInStones

def test():
    testCases = [
        {
            "input": {
                "J": "aA",
                "S": "aAAbbbb"
            },
            "output": 3
        },
        {
            "input": {
                "J": "z",
                "S": "ZZ"
            },
            "output": 0
        },
    ]
    for testCase in testCases:
        expected = testCase["output"]
        result = Solution().numJewelsInStones(testCase["input"]["J"], testCase["input"]["S"])
        assert expected == result, "Expected: {0} Got: {1}".format(expected, result)

if __name__ == "__main__":
    test()        