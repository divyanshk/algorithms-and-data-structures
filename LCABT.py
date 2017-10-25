# Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        # assumes both nodes are present in the tree
        
        if not root:
            return None
        
        if root == p or root == q:
            return root
    
        leftChild = self.lowestCommonAncestor(root.left, p, q)
        rightChild = self.lowestCommonAncestor(root.right, p, q)
        
        if leftChild and rightChild:
            return root
        
        return leftChild if leftChild else rightChild
        
        return None
