"""
Problem: Binary Tree Preorder Traversal

LeetCode: #144
Difficulty: Easy
Roadmap Topic: Trees
GitHub Folder: Trees
Pattern: DFS (Preorder Traversal)

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
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        from typing import List, Optional
        answer = []
        def preorder(node):
            if node is None:
                return
            answer.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return answer