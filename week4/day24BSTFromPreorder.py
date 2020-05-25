# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rightNodeIndex(self, array, rootNodeValue):
        """
        Assumptions: The root value does not exist in the array
        """
        index = None
        for (innerIndex, value) in enumerate(array):
            if value >= rootNodeValue:
                return innerIndex

    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = None
        if preorder:
            root = TreeNode(preorder[0])
            rightIndex = self.rightNodeIndex(preorder[1:], root.val)
            rightIndex = (rightIndex + 1) if rightIndex != None else len(preorder)
            # print(preorder, rightIndex)
            root.left = self.bstFromPreorder(preorder[1:rightIndex])
            root.right = self.bstFromPreorder(preorder[rightIndex:])
        return root
