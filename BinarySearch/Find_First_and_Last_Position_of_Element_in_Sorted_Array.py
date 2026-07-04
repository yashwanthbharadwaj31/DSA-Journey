"""
Problem: Find First and Last Position of Element in Sorted Array

LeetCode: #34
Difficulty: Medium
Topic: Binary Search
Pattern: Binary Search on Boundaries

Time Complexity: O(log n)
Space Complexity: O(1)

Date Solved: 04-07-2026
"""
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1
        # Find first occurrence
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                first = middle
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        # Find last occurrence
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                last = middle
                left = middle + 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return [first, last]