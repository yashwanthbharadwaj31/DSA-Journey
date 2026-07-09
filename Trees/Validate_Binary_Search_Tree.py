"""
Problem: Validate Binary Search Tree

LeetCode: #98
Difficulty: Medium
Roadmap Topic: Trees
GitHub Folder: Trees
Pattern: DFS + Bounds

Time Complexity: O(n)
Space Complexity: O(h)

Date Solved: 09-07-2026
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if node is None:
                return True
            if not (low < node.val < high):
                return False
            return (
                validate(node.left, low, node.val)
                and
                validate(node.right, node.val, high)
            )
        return validate(root, float("-inf"), float("inf"))