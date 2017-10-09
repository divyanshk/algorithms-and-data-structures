# Problem: https://leetcode.com/problems/sort-list/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def merge(self, leftSort, rightSort):
        headSorted = ListNode(0)
        cur = headSorted
        while (leftSort and rightSort):
            if leftSort.val < rightSort.val:
                cur.next = leftSort
                leftSort = leftSort.next
            else:
                cur.next = rightSort
                rightSort = rightSort.next
            cur = cur.next
        if leftSort:
            cur.next = leftSort
        if rightSort:
            cur.next = rightSort
        return headSorted.next
    
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # merge sort
        if not head or not head.next:
            return head
        slow = head
        fast = head
        while (fast != None and fast.next != None):
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        leftSort = self.sortList(head)
        rightSort = self.sortList(slow)
        return self.merge(leftSort, rightSort)
