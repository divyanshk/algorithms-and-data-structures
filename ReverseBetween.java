/**
 * Problem: https://leetcode.com/problems/reverse-linked-list-ii/description/
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode pre = dummy, then, start;
        for (int i=0; i<m-1; ++i) pre=pre.next;
        start=pre.next;
        then=start.next;
        for (int i=0; i<n-m; ++i) {
            start.next=then.next;
            then.next=pre.next;
            pre.next=then;
            then=start.next;
        }
        return dummy.next;
    }
}
