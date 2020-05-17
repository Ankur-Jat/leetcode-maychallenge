"""
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. Since each version is developed 
based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""
def isBadVersion(n):
    if (n > 3):
        return True
    return False

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        firstBadVersion = n
        start = 1
        end = n
        while (start < end):
            new_n = (start + end) / 2
            if (isBadVersion(new_n)):
                # Go to the left
                firstBadVersion = new_n
                end = new_n
            else:
                # Go to the right
                start = new_n + 1
        return firstBadVersion

def test():
    testCases = [
        {
            "input": 5,
            "output": 4
        },
    ]
    for testCase in testCases:
        expected = testCase["output"]
        result = Solution().firstBadVersion(testCase["input"])
        assert expected == result, "Expected: {0} Got: {1}".format(expected, result)

if __name__ == "__main__":
    test()