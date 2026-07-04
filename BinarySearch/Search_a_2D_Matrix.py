"""
Problem: Search a 2D Matrix

LeetCode: #74
Difficulty: Medium
Topic: Binary Search
Pattern: Binary Search on Matrix

Time Complexity: O(log(m × n))
Space Complexity: O(1)

Date Solved: 04-07-2026
"""
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols - 1
        while left <= right:
            middle = (left + right) // 2
            row = middle // cols
            col = middle % cols
            value = matrix[row][col]
            if value == target:
                return True
            elif value < target:
                left = middle + 1
            else:
                right = middle - 1
        return False