"""
You are given a sorted array consisting of only integers where every element appears exactly twice, 
except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

=> Best way would be comparing as array is sorted. Because that way we may get result without complete traversing.
"""

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :Assumptions: assuming nums is an non empty array
        """
        singleElement = nums[0]
        for num in nums[1:]:
            singleElement ^= num
        return singleElement
        
def test():
    testCases = [
        {
            "input": [1,1,2,3,3,4,4,8,8],
            "output": 2
        },
        {
            "input": [3,3,7,7,10,11,11],
            "output": 101
        },
    ]
    for testCase in testCases:
        expected = testCase["output"]
        result = Solution().singleNonDuplicate(testCase["input"])
        assert expected == result, "Expected: {0} Got: {1}".format(expected, result)

if __name__ == "__main__":
    test()