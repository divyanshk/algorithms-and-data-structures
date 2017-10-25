# Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
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
        cur = root
        if p.val > q.val:
            p, q = q, p
        while (cur != None):
            if cur.val >= p.val and cur.val <= q.val:
                return cur
            elif cur.val > p.val and cur.val > q.val:
                cur = cur.left
            else:
                cur = cur.right
        return None
