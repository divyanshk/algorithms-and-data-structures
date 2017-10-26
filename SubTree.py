# Problem: https://leetcode.com/problems/subtree-of-another-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isMatch(self, s, t):
        if not s and not t:
            return True 
        elif not s or not t:
            return False
        
        if s.val != t.val:
            return False
        
        left = self.isMatch(s.left, t.left)
        right = self.isMatch(s.right, t.right)
        if left and right:
            return True
        
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        if not s:
            return False
        
        if self.isMatch(s, t):
            return True
        left = self.isSubtree(s.left, t)
        right = self.isSubtree(s.right, t)
        return True if left or right else False
