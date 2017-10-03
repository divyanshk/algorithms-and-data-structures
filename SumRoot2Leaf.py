# Problem: https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recurse(self, root, runningSum):
        # base case
        # reached a leaf
        sum = 0
        if (root.left == None and root.right == None):
            return runningSum*10+root.val
        if root.left:
            sum += self.recurse(root.left, runningSum*10+root.val)
        if root.right:
            sum += self.recurse(root.right, runningSum*10+root.val)
        return sum
    
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return self.recurse(root, 0)
