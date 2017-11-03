# Problem: https://leetcode.com/problems/find-duplicate-subtrees/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traversal(self, root, map, res):
        if not root:
            # to differentiate between 00# and 0#0
            return '#'
        hash = str(root.val) + self.traversal(root.left, map, res) + self.traversal(root.right, map, res)
        if hash not in map:
            map[hash] = 1
        else:
            if map[hash] == 1:
                res.append(root)
            map[hash] += 1
        return hash
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        # post order traversal + hashmap
        map = {}
        res = []
        self.traversal(root, map, res)
        return res
