/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 
// Given a binary tree, find the maximum path sum.
//
// For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.
//
// For example:
// Given the below binary tree,
//
//        1
//       / \
//      2   3
// Return 6.


public class Solution {
	private int mps = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
    	if(root == null){
    		return 0;
    	}
    	maxPathRec(root);
    	return this.mps;

    }
    public int maxPathRec(TreeNode root) {
    	if(root == null){
    		return 0;
    	}

    	int left = maxPathRec(root.left);
    	int right = maxPathRec(root.right);
    	int sum = left + right + root.val;
    	int leftOnly = left + root.val;
    	int rightOnly = right + root.val;
    	int meOnly = root.val;
    	this.mps = Math.max(Math.max(Math.max(leftOnly, rightOnly), Math.max(meOnly,sum)),this.mps);
    	return Math.max((Math.max(left, right) + root.val), root.val);

    }
}
