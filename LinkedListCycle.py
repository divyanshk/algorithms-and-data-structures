# Problem: https://leetcode.com/problems/linked-list-cycle-ii/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next:
            return None
        fast = head
        slow = head
        
        slow = slow.next
        fast = fast.next.next
        while (slow != fast and fast!= None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        
        if not fast:
            return None
        
        # slow and fast meet. yay !
        fast = fast.next
        k = 1
        while (slow != fast and fast != None):
            fast = fast.next
            k += 1
        
        # slow and fast meet again. yay !
        # now we know the length of the cycle k
        
        pointer = head
        while(k):
            pointer = pointer.next
            k -= 1
            
        anotherPointer = head
        while (anotherPointer != pointer and anotherPointer != None and pointer != None):
            anotherPointer = anotherPointer.next
            pointer = pointer.next
            
        # this is the cycle's beginning
        return pointer
