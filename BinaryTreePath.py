# Problem: https://leetcode.com/problems/binary-tree-paths/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePathsUtil(self, root, lis, res):
        if not root:
            return
        if not root.left and not root.right:
            lis.append(str(root.val))
            res.append('->'.join(lis[:]))
            lis.pop()
            return
        lis.append(str(root.val))
        self.binaryTreePathsUtil(root.left, lis, res)
        self.binaryTreePathsUtil(root.right, lis, res)
        lis.pop()
        
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        self.binaryTreePathsUtil(root, [], res)
        return res
