# Problem: https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSumUtil(self, root, maxSoFar):
        """
        :type root: TreeNode
        :type maxSoFar: int
        :rtype: int
        """
        if not root:
            return 0
        left = self.maxPathSumUtil(root.left, maxSoFar)
        right = self.maxPathSumUtil(root.right, maxSoFar)
        left = left if left > 0 else 0
        right = right if right > 0 else 0
        sumIncludingRoot = left + right + root.val
        maxSoFar[0] = sumIncludingRoot if sumIncludingRoot > maxSoFar[0] else maxSoFar[0]
        return left + root.val if left > right else right + root.val
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxSoFar = [-float('inf')]
        self.maxPathSumUtil(root, maxSoFar)
        return maxSoFar[0]
