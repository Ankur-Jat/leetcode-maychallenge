"""
Given an array of size n, find the majority element. The majority element is the element that appears 
more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Base case
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        majortyElement = nums[0]
        majortyCount = 1
        counter = 1
        while counter < len(nums):
            if nums[counter] == majortyElement:
                majortyCount += 1
            else:
                majortyCount -= 1
                if majortyCount == 0:
                    majortyElement = nums[counter]
                    majortyCount += 1
            counter += 1
        # Check if the majrotyElement count is really more than n/2
        majortyCount = 0
        majortyCount = len(filter(lambda num: num == majortyElement, nums))
        if majortyCount > (len(nums) / 2):
            return majortyElement
        return None

def test():
    testCases = [
        {
            "input": [3,2,3],
            "output": 3
        },
        {
            "input": [2,2,1,1,1,2,2],
            "output": 2
        },
    ]
    for testCase in testCases:
        expected = testCase["output"]
        result = Solution().findComplement(testCase["input"])
        assert expected == result, "Expected: {0} Got: {1}".format(expected, result)

if __name__ == "__main__":
    test()