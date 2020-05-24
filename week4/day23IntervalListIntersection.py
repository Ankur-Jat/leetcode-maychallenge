"""
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

Input: A = [[0,2],[5,10],[13,23],[24,25]], 
       B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
"""
class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        list1StartIndex = 0
        list2StartIndex = 0
        intervals = []
        while list1StartIndex < len(A) and list2StartIndex < len(B):
            intervalStarting, intervalEnding = max(A[list1StartIndex][0], B[list2StartIndex][0]),  min(A[list1StartIndex][1], B[list2StartIndex][1])
            if intervalStarting <= intervalEnding:
                intervals.append([intervalStarting, intervalEnding])
            if A[list1StartIndex][1] < B[list2StartIndex][1]:
                list1StartIndex += 1
            else:
                list2StartIndex += 1
        return intervals

def test():
    
    testCases = [
        {
            "input": {
                "A": [[0,2],[5,10],[13,23],[24,25]],
                "B": [[1,5],[8,12],[15,24],[25,26]],
            },
            "output": [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
        },
        {
            "input": {
                "A": [[1, 3]],
                "B": [[2, 4]],
            },
            "output": [[2, 3]]
        },
    ]
    for testCase in testCases:
        expected = testCase["output"]
        result = Solution().intervalIntersection(testCase["input"]["A"], testCase["input"]["B"])
        assert expected == result, "Expected: {0} Got: {1}".format(expected, result)

if __name__ == "__main__":
    test()
