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
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        xLevel, xParent = self.findNodeLevelAndParent(root, x, 0, None)
        yLevel, yParent = self.findNodeLevelAndParent(root, y, 0, None)
        # Assuming that x, and y are present and 
        if not xParent or not yParent:
            # Becuase this is the case where x or y is root.
            return False
        if xLevel == yLevel and xParent.val != yParent.val:
            return True
        return False

    def findNodeLevelAndParent(self, root, nodeValue, currentLevel, parent):
        if (root.val == nodeValue):
            return (currentLevel, parent)
        isInLeftNode = isInRightNode = (None, None)
        level = None
        if (root.left):
            isInLeftNode = self.findNodeLevelAndParent(root.left, nodeValue, currentLevel+1, root)
        if not isInLeftNode[0] and root.right:
            isInRightNode = self.findNodeLevelAndParent(root.right, nodeValue, currentLevel+1, root)
        # print(isInLeftNode, isInRightNode, root.val)
        return isInLeftNode if isInLeftNode[0] else isInRightNode if isInRightNode[0] else (None, None)

def test():

    testCases = [
        {
            "input": {
                "root": Node(1).setLeft(Node(2).setLeft(Node(4))).setRight(Node(3)),
                "x": 4,
                "y": 3
            },
            "output": False
        },
        {
            "input": {
                "root": Node(1).setLeft(Node(2).setRight(Node(4))).setRight(Node(3).setRight(Node(5))),
                "x": 5,
                "y": 4
            },
            "output": True
        },
        {
            "input": {
                "root": Node(1).setLeft(Node(2).setRight(Node(4))).setRight(Node(3)),
                "x": 2,
                "y": 3
            },
            "output": False
        },
    ]
    for testCase in testCases:
        expected = testCase["output"]
        result = Solution().isCousins(testCase["input"]["root"], testCase["input"]["x"], testCase["input"]["y"])
        assert expected == result, "Expected: {0} Got: {1}".format(expected, result)

if __name__ == "__main__":
    test()
