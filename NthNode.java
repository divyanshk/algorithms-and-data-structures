/**
 * Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode node1 = head, node2 = head, temp = head;
        while(node1!=null && n!=0) {
            node1 = node1.next;
            n--;
        }
        if (node1==null) 
            return head.next;
        else {
            while(node1!=null) {
                node1=node1.next;
                temp=node2;
                node2=node2.next;
            }
            temp.next=node2.next;
            return head;
        }
    }
}
