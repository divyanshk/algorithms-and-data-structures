# Problem: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traversal(self, root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        node = root
        tempRight = root.right
        root.right = self.traversal(root.left)
        root.left = None
        while(node.left or node.right):
            node = node.right
        node.right = self.traversal(tempRight)
        return root
        
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.traversal(root)
        # return nothing        
