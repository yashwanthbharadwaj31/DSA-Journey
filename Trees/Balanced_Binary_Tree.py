"""
Problem: Balanced Binary Tree

LeetCode: #110
Difficulty: Easy
Roadmap Topic: Trees / Recursion
GitHub Folder: Trees
Pattern: DFS + Bottom-Up Recursion

Time Complexity: O(n)
Space Complexity: O(h)

Date Solved: 08-07-2026
"""
from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0
            leftHeight = height(node.left)
            if leftHeight == -1:
                return -1
            rightHeight = height(node.right)
            if rightHeight == -1:
                return -1
            if abs(leftHeight - rightHeight) > 1:
                return -1
            return 1 + max(leftHeight, rightHeight)
        return height(root) != -1