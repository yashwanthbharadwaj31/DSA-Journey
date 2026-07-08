"""
Problem: Diameter of Binary Tree

LeetCode: #543
Difficulty: Easy
Roadmap Topic: Trees
GitHub Folder: Trees
Pattern: DFS + Postorder Traversal

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def depth(node):
            nonlocal diameter
            if node is None:
                return 0
            leftDepth = depth(node.left)
            rightDepth = depth(node.right)
            diameter = max(diameter, leftDepth + rightDepth)
            return 1 + max(leftDepth, rightDepth)
        depth(root)
        return diameter