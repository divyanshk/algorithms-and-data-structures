# Problem: https://leetcode.com/problems/house-robber-iii/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def robUtil(self, root):
        """
	:type root: TreeNode
	:rtype: (included, excluded)
        """ 
	# DP + DFS
        
        if not root:
            return (0, 0)
        
        left = self.robUtil(root.left)
        right = self.robUtil(root.right)
        
        exc = max(left[0], left[1]) + max(right[0], right[1])
        inc = root.val + left[0] + right[0]
        
        return (exc, inc)
    
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        exc, inc = self.robUtil(root)
        return max(exc, inc)
