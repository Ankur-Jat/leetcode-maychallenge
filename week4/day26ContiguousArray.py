class Solution(object):
    def mainLogic(self, nums):
        numberStack = []
        maxRangeStack = []
        maxSoFar = 0
        carry = 0
        # print(nums)
        for num in nums:
            print("pre", num, numberStack, maxRangeStack, carry)
            if not numberStack:
                print("Empty stack")
                numberStack.append(num)
                maxRangeStack.append(carry)
            else:
                carry = 0
                if num == numberStack[-1]:
                    numberStack.append(num)
                    maxRangeStack.append(0)
                    print("new number is same as last")
                else:
                    print("new number is different")
                    lastNum = numberStack.pop()
                    currentMaxSoFar = maxRangeStack.pop()
                    tempMaxSoFar = 2 + currentMaxSoFar
                    if maxRangeStack:
                        maxRangeStack[-1] = maxRangeStack[-1] + tempMaxSoFar
                    else:
                        carry = tempMaxSoFar
                    maxSoFar = max(maxSoFar, tempMaxSoFar, maxRangeStack[-1] if maxRangeStack else 0, carry)
            print("post", num, numberStack, maxRangeStack, maxSoFar, carry)
        return maxSoFar

    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return max(self.mainLogic(nums), self.mainLogic(nums[::-1]))
        return self.mainLogic(nums[::-1])
        return self.mainLogic(nums)

# a = [1,1,1,1,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,1,1,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,0,0,1,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,0,0,1,0,1,1]
# print(Solution().findMaxLength(a))
# b = [0,0,1,0,0,0,1,1]
# print(Solution().findMaxLength(b))
c = [0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]
print(Solution().findMaxLength(c))
