/**
 * Problem: https://leetcode.com/problems/binary-tree-inorder-traversal/description/
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    void inorderTraversalUtil(TreeNode root, List<Integer> res) {
        if (root==null) return;
        inorderTraversalUtil(root.left, res);
        res.add(root.val);
        inorderTraversalUtil(root.right, res);
    }
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        inorderTraversalUtil(root, res);
        return res;
    }
}
