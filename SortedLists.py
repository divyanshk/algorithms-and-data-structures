# https://leetcode.com/problems/merge-two-sorted-lists/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp1, tmp2 = l1, l2
        tmp3 = ListNode(-1)
        start = tmp3
        while(tmp1 or tmp2):
            if(tmp1 and tmp2):
                if tmp1.val <= tmp2.val:
                    tmp3.next = tmp1
                    tmp1 = tmp1.next
                else:
                    tmp3.next = tmp2
                    tmp2 = tmp2.next
                tmp3 = tmp3.next
            else:
                if tmp1:
                    tmp3.next = tmp1
                else:
                    tmp3.next = tmp2
                tmp3 = tmp3.next
                break
        return start.next            
