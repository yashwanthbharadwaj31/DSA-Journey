"""
Problem: Binary Search

LeetCode: #704
Difficulty: Easy
Topic: Binary Search
Pattern: Binary Search

Time Complexity: O(log n)
Space Complexity: O(1)

Date Solved: 03-07-2026
"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1