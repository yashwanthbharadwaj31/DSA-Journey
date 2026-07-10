"""
Problem: Count Complete Tree Nodes

LeetCode: #222
Difficulty: Easy
Roadmap Topic: Trees
GitHub Folder: Trees
Pattern: DFS (Recursion)

Time Complexity: O(n)
Space Complexity: O(h)

Date Solved: 10-07-2026
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        from typing import Optional
        if root is None:
            return 0
        leftCount = self.countNodes(root.left)
        rightCount = self.countNodes(root.right)
        return 1 + leftCount + rightCount