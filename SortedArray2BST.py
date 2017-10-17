# Problem: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBSTUtil(self, nums, start, end):
        if start > end:
            return None
        mid = start + (end-start)/2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBSTUtil(nums, start, mid-1)
        root.right = self.sortedArrayToBSTUtil(nums, mid+1, end)
        return root
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.sortedArrayToBSTUtil(nums, 0, len(nums)-1)
