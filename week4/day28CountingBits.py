class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        dpMatrix = [0 for _ in range(num + 1)]
        dpMatrix[1] = 1
        for number in range(2, num + 1):
            if number % 2 == 0:
                # Even number
                dpMatrix[number] = dpMatrix[number >> 1]
            else:
                # Odd number
                dpMatrix[number] = dpMatrix[number >> 1] + 1
        return dpMatrix


def testSolution():
    testCases = [
        {
            "input": 0,
            "output": [0]
        },
        {
            "input": 1,
            "output": [0, 1]
        },
        {
            "input": 2,
            "output": [0, 1, 1]
        },
        {
            "input": 4,
            "output": [0, 1, 1, 2, 1]
        },
        {
            "input": 13,
            "output": [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3]
        }
    ]

    solution = Solution()
    for testCase in testCases:
        output = solution.countBits(testCase["input"])
        assert output == testCase["output"], "FAILED! For Input: {}, Expected: {}, Got: {}"\
            .format(testCase["input"], testCase["output"], output)


if __name__ == "__main__":
    testSolution()