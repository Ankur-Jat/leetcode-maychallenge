"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number 
is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
"""

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == 0:
            return "0"
        if k == 0:
            return num
        if k >= len(num):
            return "0"
        start_index = 0
        while k > 0 and len(num):
            """
            "1432219", k = 3
            0 => 132219 => 1 => 2 
            1 => 12219 => 1 => 1
            2 => 1219 => 1 => 0
            123456789, k=3
            0 => 
            """
            while start_index < len(num) - 1 and num[start_index] <= num[start_index+1]:
                start_index += 1
            num = num[0:start_index] + num[start_index+1:]
            start_index = max(start_index -1, 0)
            while num and num[0] == "0":
                num = num[1:]
            k -= 1
            # This will save empty while loop iterations
            if start_index == len(num) and k > 0:
                num = num[0:len(num) - k]
                break
        if len(num) == 0:
            num = "0"
        return num

def test():
    testCases = [
        {
            "input": {
                "num": "1432219",
                "k": 3
            },
            "output": "1219"
        },
        {
            "input": {
                "num": "10200",
                "k": 1
            },
            "output": "200"
        },
        {
            "input": {
                "num": "10",
                "k": 2
            },
            "output": "0"
        },
    ]
    for testCase in testCases:
        expected = testCase["output"]
        result = Solution().removeKdigits(testCase["input"])
        assert expected == result, "Expected: {0} Got: {1}".format(expected, result)

if __name__ == "__main__":
    test()