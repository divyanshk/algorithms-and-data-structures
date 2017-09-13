/**
 * Problem: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
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
    public TreeNode helper(int[] inorder, int[] postorder, int postEnd, int inStart, int inEnd) {
        if (postEnd > postorder.length - 1 || inStart > inEnd || postEnd < 0) return null;
        TreeNode root = new TreeNode(postorder[postEnd]);
        int inIndex = indexInMap.get(root.val); // index of the root in inorder
        root.left = helper(inorder, postorder, postEnd-inEnd+inIndex-1, inStart, inIndex-1);
        root.right = helper(inorder, postorder, postEnd-1, inIndex+1, inEnd);
        return root;
    }
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        indexInMap = new HashMap<Integer, Integer>();
        mapInIndex(inorder);
        return helper(inorder, postorder, postorder.length-1, 0, inorder.length-1);
    }
}
