# Problem: https://leetcode.com/problems/insertion-sort-list/discuss/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        cur = head.next
        prev = head
        curr = dummy
        while (cur):
            if cur.val < prev.val:
                while (curr.next.val < cur.val):
                    curr = curr.next
                prev.next = cur.next
                cur.next = curr.next
                curr.next = cur
                curr = dummy # reset curr
            else:
                prev = cur
            cur = prev.next
        return dummy.next
