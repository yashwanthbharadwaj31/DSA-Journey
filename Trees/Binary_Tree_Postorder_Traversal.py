"""
Problem: Binary Tree Postorder Traversal

LeetCode: #145
Difficulty: Easy
Roadmap Topic: Trees
GitHub Folder: Trees
Pattern: DFS (Postorder Traversal)

Time Complexity: O(n)
Space Complexity: O(h)

Date Solved: 11-07-2026
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        from typing import List, Optional
        answer = []
        def postorder(node):
            if node is None:
                return
            postorder(node.left)
            postorder(node.right)
            answer.append(node.val)
        postorder(root)
        return answer