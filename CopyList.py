# Problem: https://leetcode.com/problems/copy-list-with-random-pointer/description/
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        
        pointerMap = {}
        headc = RandomListNode(head.label)
        pointerMap[head] = headc
        
        cur = headc
        curOrg = head
        while curOrg.next:
            curOrg = curOrg.next
            cur.next = RandomListNode(curOrg.label)
            cur = cur.next
            pointerMap[curOrg] = cur
        cur.next = None
        
        cur = head
        while cur:
            if cur.random:
                pointerMap[cur].random = pointerMap[cur.random]
            cur = cur.next
            
        return headc
