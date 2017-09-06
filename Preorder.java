/**
 * Problem: https://leetcode.com/problems/binary-tree-preorder-traversal/description/
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    void preorderTraversalUtil(TreeNode root, List<Integer> res) {
        if (root==null) return;
        res.add(root.val);
        preorderTraversalUtil(root.left, res);
        preorderTraversalUtil(root.right, res);
    }
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        preorderTraversalUtil(root, res);
        return res;
    }
}
