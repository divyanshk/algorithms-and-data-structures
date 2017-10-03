# Problem: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
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
        # move down each level, set up the connection between siblings
        # use that connection in the next level to move to cousins
        cur_level = root
        cur = None
        while (cur_level):
            cur = cur_level
            while(cur.left):
                cur.left.next = cur.right
                if (cur.next):
                    cur.right.next = cur.next.left
                    cur = cur.next
                else:
                    break
            cur_level = cur_level.left
