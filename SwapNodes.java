/**
 * Problem: https://leetcode.com/problems/swap-nodes-in-pairs/
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode i=head,j,k=head;
        if (head==null) return null;
        while (i!=null && i.next!=null) {
            j=i.next;
            i.next=j.next;
            j.next=i;
            if (i==head) 
                head=j;
            else
                k.next=j;
            k=i;
            i=i.next;
        }
        return head;
    }
}
