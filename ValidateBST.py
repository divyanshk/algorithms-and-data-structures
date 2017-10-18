# Problem: https://leetcode.com/problems/validate-binary-search-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return self.isValidBSTUtil(root)[0]
        
    def isValidBSTUtil(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Base case: leaf node is a valid BST
        if (not root.left and not root.right):
            return (True, root.val, root.val)
        
        # Both childs are present or one of them
        if root.left:
            isLeft, leftMin, leftMax = self.isValidBSTUtil(root.left)
        else:
            # empty 
            isLeft, leftMin, leftMax = True, float('inf'), float('-inf')
        if root.right:
            isRight, rightMin, rightMax = self.isValidBSTUtil(root.right)
        else:
            # empty
            isRight, rightMin, rightMax = True, float('inf'), float('-inf')
                
        isBST = isLeft and isRight and (leftMax < root.val) and (root.val < rightMin)
        return (isBST, leftMin if leftMin < root.val else root.val,\
                rightMax if rightMax > root.val else root.val)
