# Problem: https://leetcode.com/problems/merge-k-sorted-lists/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = []
        if not lists:
            return []
        
        for l in lists:
            if l:
                heapq.heappush(h, (l.val, l))
            
        if not h:
            return []
        root = heapq.heappop(h)[1]
        curr = root
        while h:
            if curr.next is not None:
                heapq.heappush(h, (curr.next.val, curr.next))
                
            curr.next = heapq.heappop(h)[1]
            curr = curr.next
        
        return root
