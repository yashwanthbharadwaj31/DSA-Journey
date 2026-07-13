"""
Problem: Construct Binary Tree from Preorder and Inorder Traversal

LeetCode: #105
Difficulty: Medium
Roadmap Topic: Trees
GitHub Folder: Trees
Pattern: DFS + Divide & Conquer + HashMap

Time Complexity: O(n)
Space Complexity: O(n)

Date Solved: 13-07-2026
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIndex = {}
        for index, value in enumerate(inorder):
            inorderIndex[value] = index
        preorderIndex = 0
        def build(left, right):
            nonlocal preorderIndex
            if left > right:
                return None
            rootValue = preorder[preorderIndex]
            preorderIndex += 1
            root = TreeNode(rootValue)
            mid = inorderIndex[rootValue]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root
        return build(0, len(inorder) - 1)