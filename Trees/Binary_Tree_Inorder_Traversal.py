"""
Problem: Binary Tree Inorder Traversal

LeetCode: #94
Difficulty: Easy
Topic: Trees
Pattern: DFS (Inorder Traversal)

Time Complexity: O(n)
Space Complexity: O(n)

Date Solved: 06-07-2026
"""
from typing import List, Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            answer.append(node.val)
            inorder(node.right)
        inorder(root)
        return answer