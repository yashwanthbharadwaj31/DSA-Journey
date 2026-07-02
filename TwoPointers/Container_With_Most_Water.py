"""
Problem: Container With Most Water

LeetCode: #11
Difficulty: Medium
Topic: Two Pointers
Pattern: Two Pointers + Greedy

Time Complexity: O(n)
Space Complexity: O(1)

Date Solved: 02-07-2026
"""
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maximum = 0
        while left < right:
            width = right - left
            if height[left] < height[right]:
                current = height[left] * width
            else:
                current = height[right] * width
            if current > maximum:
                maximum = current
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maximum