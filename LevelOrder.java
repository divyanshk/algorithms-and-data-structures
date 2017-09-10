/**
 * Problem: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> order = new ArrayList<List<Integer>>();
        if (root == null) return order;
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        List<Integer> res = new ArrayList<Integer>();
        int parentQueueSize=0, childQueueSize=0;a
        queue.add(root);
        parentQueueSize++;
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            parentQueueSize--;
            res.add(node.val);
            if (node.left != null) {
                queue.add(node.left);
                childQueueSize++;
            }
            if (node.right != null) {
                queue.add(node.right);
                childQueueSize++;
            }
            if (parentQueueSize == 0) {
                parentQueueSize = childQueueSize;
                childQueueSize = 0;
                order.add(res);
                res = new ArrayList<Integer>();
            }
        }
        return order;
    }
}
