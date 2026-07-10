"""
Problem: Binary Tree Right Side View

LeetCode: #199
Difficulty: Medium
Roadmap Topic: Trees
GitHub Folder: Trees
Pattern: DFS (Right First)

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from typing import List, Optional
        answer = []
        def dfs(node, level):
            if node is None:
                return
            if level == len(answer):
                answer.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        dfs(root, 0)
        return answers