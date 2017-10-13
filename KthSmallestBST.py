# Problem: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # call countNodes on the left child
        count = self.countNodes(root.left)
        if count+1 == k:
            return root.val
        elif count+1 > k:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k-count-1)
