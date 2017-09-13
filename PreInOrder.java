/**
 * Problem: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    int MAX=10000;
    Map<Integer, Integer> indexInMap;
    public void mapInIndex(int[] inorder) {
        for (int i=0; i<inorder.length; ++i) {
            indexInMap.put(inorder[i], i);
        }
    }
    public TreeNode helper(int[] preorder, int[] inorder, int preStart, int inStart, int inEnd) {
        if (preStart > preorder.length - 1 || inStart > inEnd) return null;
        TreeNode root = new TreeNode(preorder[preStart]);
        int inIndex = indexInMap.get(root.val); // index of the root in inorder
        root.left = helper(preorder, inorder, preStart+1, inStart, inIndex-1);
        root.right = helper(preorder, inorder, preStart+inIndex-inStart+1, inIndex+1, inEnd);
        return root;
    }
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        indexInMap = new HashMap<Integer, Integer>();
        mapInIndex(inorder);
        return helper(preorder, inorder, 0, 0, inorder.length-1);
    }
}
