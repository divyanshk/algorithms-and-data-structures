# https://leetcode.com/contest/weekly-contest-94/problems/leaf-similar-trees/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inOrder(self, root, seq):
        if root.left:
            seq = self.inOrder(root.left, seq)
        if root.right:
            seq = self.inOrder(root.right, seq)
        if not root.left and not root.right:
            seq.append(root.val)
        return seq
    
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return (self.inOrder(root1, []) == self.inOrder(root2, []))
