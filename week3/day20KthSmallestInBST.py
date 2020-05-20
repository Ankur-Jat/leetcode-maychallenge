# -*- coding: UTF-8 -*-
"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1


Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
"""
class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
    
    def setLeft(self, node):
        self.left = node
        return self
    
    def setRight(self, node):
        self.right = node
        return self

class Solution(object):
    def getInOrder(self, root, traverseData=None):
        if traverseData == None:
            traverseData = []
        if root:
            if root.left:
                self.getInOrder(root.left, traverseData)
            traverseData.append(root.val)
            if root.right:
                self.getInOrder(root.right, traverseData)
        return traverseData
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        inOrderTraversal = self.getInOrder(root)
        return inOrderTraversal[k - 1]
        
def test():

    testCases = [
        {
            "input": {
                "root": Node(3).setLeft(Node(1).setRight(Node(2))).setRight(Node(4)),
                "k": 1,
            },
            "output": 1
        },
        {
            "input": {
                "root": Node(5).setLeft(Node(3).setLeft(Node(2).setLeft(Node(1))).setRight(Node(4))).setRight(Node(6)),
                "k": 3,
            },
            "output": 3
        },
    ]
    for testCase in testCases:
        expected = testCase["output"]
        result = Solution().kthSmallest(testCase["input"]["root"], testCase["input"]["k"])
        assert expected == result, "Expected: {0} Got: {1}".format(expected, result)

if __name__ == "__main__":
    test()
