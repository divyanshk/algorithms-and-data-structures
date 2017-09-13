/**
 * Problem: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode helper(ListNode head, ListNode tail) {
        ListNode slow=head, fast=head;
        TreeNode root;
        if (head==tail) return null;
        while (fast!=tail&&fast.next!=tail) {
            slow=slow.next;
            fast=fast.next.next;
        }
        root = new TreeNode(slow.val);
        root.left = helper(head, slow);
        root.right = helper(slow.next, tail);
        return root;
    }
    public TreeNode sortedListToBST(ListNode head) {
        TreeNode root = helper(head, null);
        return root;
    }
}
