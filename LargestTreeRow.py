# Problem: https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        maxSoFar = float('-inf')
        maxValues, queue = [], []
        queue.append(root)
        numChild, numParents = 0, 1
        while queue:
            item = queue.pop(0)
            numParents -= 1
            if item.val > maxSoFar:
                maxSoFar = item.val
            if item.left:
                queue.append(item.left)
                numChild += 1
            if item.right:
                queue.append(item.right)
                numChild += 1
            if numParents == 0:
                numParents, numChild = numChild, 0
                maxValues.append(maxSoFar)
                maxSoFar = float('-inf')
        return maxValues
