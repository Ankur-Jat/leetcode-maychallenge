"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')


Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1Len = len(word1) + 1
        word2Len = len(word2) + 1
        # prepare matrix
        dpMatrix = [[0] * word2Len for _ in range(word1Len)]
        for index in range(word2Len):
            dpMatrix[0][index] = index
        for index in range(word1Len):
            dpMatrix[index][0] = index

        for (index1, char1) in enumerate(word1):
            index1 += 1
            for (index2, char2) in enumerate(word2):
                index2 += 1
                if char1 == char2:
                    # Pick the diagonal
                    dpMatrix[index1][index2] = dpMatrix[index1 - 1][index2 - 1]
                else:
                    # Pick the min
                    dpMatrix[index1][index2] = min(
                        dpMatrix[index1 -1 ][index2],
                        dpMatrix[index1][index2 - 1],
                        dpMatrix[index1 - 1][index2 - 1]
                    ) + 1
        return dpMatrix[-1][-1]

def testSolution():
    testCases = [
        {
            "input": {
                "word1": "horse",
                "word2": "ros"
            },
            "output": 3
        },
        {
            "input": {
                "word1": "intention",
                "word2": "execution"
            },
            "output": 5
        },
    ]
    
    solution = Solution()
    for testCase in testCases:
        output = solution.minDistance(testCase["input"]["word1"], testCase["input"]["word2"])
        assert output == testCase["output"], "FAILED! Expected: {}, Got: {}".format(testCase["output"], output)

if __name__ == "__main__":
    testSolution()