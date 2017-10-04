# Problem: https://leetcode.com/problems/rotate-list/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if head == None:
            return None
        
        curr = head
        n = 0
        while(curr):
            curr = curr.next
            n += 1
        
        k = k%n
        if k == 0:
            return head
        
        dummy = ListNode(0)
        curr = head
        dummy.next = head
        prev = dummy
        end = dummy
        while(k):
            if not curr:
                curr = head
                end = dummy
            curr = curr.next
            end = end.next
            k -= 1
        
        start = head
        while (curr != None):
            curr = curr.next
            end = end.next
            start = start.next
            prev = prev.next
        
        prev.next = end.next
        end.next = head
        head = start
        
        return head
        
