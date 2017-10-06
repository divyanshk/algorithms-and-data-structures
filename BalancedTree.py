# Problem:https://leetcode.com/problems/balanced-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalancedHeightUtil(self, root):
        if not root:
            return (True, 0)
        
        leftChildRecurse = self.isBalancedHeightUtil(root.left)
        rightChildRecurse = self.isBalancedHeightUtil(root.right)
        
        rootHeight = 1 + max(leftChildRecurse[1], rightChildRecurse[1])
        isHeightBalanced = (abs(leftChildRecurse[1] - rightChildRecurse[1])) < 2
        isRootBalanced = isHeightBalanced and leftChildRecurse[0] and rightChildRecurse[0]
        
        return (isRootBalanced, rootHeight)
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isBalancedHeightUtil(root)[0]
        
        
