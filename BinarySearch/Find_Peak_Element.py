"""
Problem: Find Peak Element

LeetCode: #162
Difficulty: Medium
Topic: Binary Search
Pattern: Binary Search on Answer

Time Complexity: O(log n)
Space Complexity: O(1)

Date Solved: 05-07-2026
"""
from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] < nums[middle + 1]:
                left = middle + 1
            else:
                right = middle
        return left