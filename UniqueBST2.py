# Problme: https://leetcode.com/problems/unique-binary-search-trees-ii/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # lesson: cant 'store' every previous dp solution,
        # sometimes have to recurse to the previous solution
        
        if n==0:
            return []
        def generateTreesUtil(start, end):
            res = []
            for node in xrange(start, end+1):
                for left in generateTreesUtil(start, node-1):
                    for right in generateTreesUtil(node+1, end):
                        root = TreeNode(node)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res if res else [None]
        return generateTreesUtil(1, n)
