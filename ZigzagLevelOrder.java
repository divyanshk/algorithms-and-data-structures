/**
 * Problem: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.util.*;
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        boolean invert=false;
        TreeNode node;
        List<List<Integer>> order = new ArrayList<List<Integer>>();
        if (root == null) return order;
        Deque<TreeNode> queue = new LinkedList<TreeNode>();
        List<Integer> res = new ArrayList<Integer>();
        int parentQueueSize=0, childQueueSize=0;
        queue.addFirst(root);
        parentQueueSize++;
        while (!queue.isEmpty()) {
            if (!invert) {
                // invert is false
                node = queue.removeFirst();
                if (node.left != null) {
                    queue.addLast(node.left);
                    childQueueSize++;
                }
                if (node.right != null) {
                    queue.addLast(node.right);
                    childQueueSize++;
                }
            }
            else {
                // invert is true
                node = queue.removeLast();
                if (node.right != null) {
                    queue.addFirst(node.right);
                    childQueueSize++;
                }
                if (node.left != null) {
                    queue.addFirst(node.left);
                    childQueueSize++;
                }
            }
            parentQueueSize--;
            res.add(node.val);
            if (parentQueueSize == 0) {
                parentQueueSize = childQueueSize;
                childQueueSize = 0;
                order.add(res);
                res = new ArrayList<Integer>();
                invert = !invert;
            }
        }
        return order;
    }
}
