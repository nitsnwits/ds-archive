# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}

    def maxDepth(self, root):
    	if root is None:
    		return 0
    	return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))