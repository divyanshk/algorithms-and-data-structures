# Problem: https://leetcode.com/problems/maximum-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        max, max_i = -float('inf'), 0
        for i in xrange(len(nums)):
            if nums[i] > max:
                max = nums[i]
                max_i = i
        root = TreeNode(max)
        root.left = self.constructMaximumBinaryTree(nums[0:max_i])
        root.right = self.constructMaximumBinaryTree(nums[max_i+1:])
        return root
