/**
 * Problem: https://leetcode.com/problems/add-two-numbers
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry=0, sum=0;
        ListNode l3, answer = new ListNode(0);
        l3 = answer;
        while (l1 != null || l2 != null) {
            sum = 0;
            sum += (l1 == null) ? 0:l1.val;
            sum += (l2 == null) ? 0:l2.val;
            sum += carry;
            l3.val = sum%10;
            carry = sum/10;
            l1 = (l1 == null) ? l1:l1.next;
            l2 = (l2 == null) ? l2:l2.next;
            if (l1==null && l2==null)
                l3.next = null;
            else {
                l3.next = new ListNode(0);
                l3 = l3.next;
            }
        }
        if (carry != 0) {
            l3.next = new ListNode(carry);
        } 
        return answer;
    }
}
