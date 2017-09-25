# Problem: https://leetcode.com/problems/path-sum-ii/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def backtrack(self, root, sum, pathSums, tempList=None):
        if (root.left is None and root.right is None and sum == 0):
            pathSums.append(tempList[:])
            return
        if (root.left is not None):
            tempList.append(root.left.val)
            self.backtrack(root.left, sum-root.left.val, pathSums, tempList)
            tempList.pop()
        if (root.right is not None):
            tempList.append(root.right.val)
            self.backtrack(root.right, sum-root.right.val, pathSums, tempList)
            tempList.pop()
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        pathSums = []
        tempList = []
        if root is None:
            return []
        elif sum == root.val and (root.left is None and root.right is None):
            return [[root.val]] 
        tempList.append(root.val)
        self.backtrack(root, sum-root.val, pathSums, tempList)
        tempList.pop()
        return pathSums
