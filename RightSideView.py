# Problem: https://leetcode.com/problems/binary-tree-right-side-view/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    lastSeenLevel = 0
    def rightSideViewUtil(self, root, level, res):
       
        if not root:
            return None
        
        if level > self.lastSeenLevel:
            res.append(root.val)
            self.lastSeenLevel += 1
      
        if root.right:
            self.rightSideViewUtil(root.right, level+1, res)
        if root.left:
            self.rightSideViewUtil(root.left, level+1, res)
        
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root:
            return []
       
        res = []
        self.rightSideViewUtil(root, 1, res)
        return res
