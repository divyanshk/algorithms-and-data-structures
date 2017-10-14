# Problem: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return root
        prev = None
        queue = []
        queue.append(root)
        numParents, numChild = 1, 0
        while queue:
            elem = queue.pop(0)
            if prev:
                prev.next = elem
            numParents -= 1
            if elem.left:
                queue.append(elem.left)
                numChild += 1
            if elem.right:
                queue.append(elem.right)
                numChild += 1
            if numParents == 0:
                numParents, numChild = numChild, numParents
                prev = None
            else:
                prev = elem
