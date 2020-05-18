# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3331/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Main Solution
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # If LL is empty of only 1 or two nodes exist
        if head == None or head.next == None:
            return head
        
        oddPtr = head
        evenPtrStart = head.next
        evenPtr = head.next
        while evenPtr and evenPtr.next != None:
            tempPtr = evenPtr.next.next
            oddPtr.next = evenPtr.next
            oddPtr.next.next = evenPtrStart
            evenPtr.next = tempPtr
            oddPtr, evenPtr = oddPtr.next, evenPtr.next
        return head

def test():
    # method for test
    def makeLLFromList(nodeList):
        if not nodeList:
            return None
        head = ListNode(nodeList[0])
        startNode = head
        for item in nodeList[1:]:
            startNode.next = ListNode(item)
            startNode = startNode.next
        return head

    def makeListFromLL(ll):
        nodeList = []
        node = ll
        while node != None:
            nodeList.append(node.val)
            node = node.next
        return nodeList

    # Test cases
    testCases = [
        {
            "input": makeLLFromList([1,2, 3, 4, 5]),
            "output": [1, 3, 5, 2, 4]
        },
        {
            "input": makeLLFromList([2, 1, 3, 5, 6, 4, 7]),
            "output": [2, 3, 6, 7, 1, 5, 4]
        }
    ]

    for testCase in testCases:
        expected = testCase["output"]
        result = makeListFromLL(Solution().oddEvenList(testCase["input"]))
        assert result == testCase["output"], "Expected: {0}, Result: {1}".format(expected, result)

if __name__ == "__main__":
    test()