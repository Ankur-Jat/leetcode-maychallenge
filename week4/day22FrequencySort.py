class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        frequencyDict = {}
        for char in s:
            frequencyDict[char] = frequencyDict.get(char, 0) + 1
        return ''.join(
            map(
                lambda item: item[0]*item[1],
                sorted(frequencyDict.items(), key=lambda item: item[1], reverse=True)
            )
        )
        
def test():
    testCases = [
        {
            "input": "tree",
            "output": "eert"
        },
        {
            "input": "cccaaa",
            "output": "aaaccc"
        },
    ]
    for testCase in testCases:
        expected = testCase["output"]
        result = Solution().frequencySort(testCase["input"])
        assert expected == result, "Expected: {0} Got: {1}".format(expected, result)

if __name__ == "__main__":
    test()