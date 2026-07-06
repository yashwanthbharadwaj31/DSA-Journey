"""
Problem: Maximum Depth of Binary Tree

LeetCode: #104
Difficulty: Easy
Topic: Trees
Pattern: DFS (Recursion)

Time Complexity: O(n)
Space Complexity: O(n)

Date Solved: 06-07-2026
"""
from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return max(leftDepth, rightDepth) + 1