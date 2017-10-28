# Problem: https://leetcode.com/problems/delete-node-in-a-bst/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMinimumNode(self, node):
        """
        :type node: TreeNode
        :rtype: TreeNode
        """
        if not node:
            return node
        while node.left:
            node = node.left
        return node
    
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        # search for the key
        parent = None
        cur = root
        while cur:
            if cur.val == key:
                # delete cur
                break
            elif cur.val < key:
                parent = cur
                cur = cur.right
            else:
                parent = cur
                cur = cur.left
        
        if not cur:
            return root
    
        # delete cur
        # case 1: no children
        if not cur.left and not cur.right:
            # root to be deleted
            if cur == root and parent == None:
                return None

            if parent.left == cur:
                parent.left = None
            else:
                parent.right = None
        
        # case 2: one child
        elif not cur.left and cur.right:
            if parent == None:
                return cur.right
            
            if parent.left == cur:
                parent.left = cur.right
            else:
                parent.right = cur.right
                
        if not cur.right and cur.left:
            if parent == None:
                return cur.left
            if parent.left == cur:
                parent.left = cur.left
            else:
                parent.right = cur.left
                
        # case 3: two children
        elif cur.left and cur.right:
            succ = self.findMinimumNode(cur.right)
            cur.val = succ.val
            cur.right = self.deleteNode(cur.right, succ.val)
         
        return root
