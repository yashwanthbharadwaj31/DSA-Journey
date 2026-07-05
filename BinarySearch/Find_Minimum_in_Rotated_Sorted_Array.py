"""
Problem: Find Minimum in Rotated Sorted Array

LeetCode: #153
Difficulty: Medium
Topic: Binary Search
Pattern: Modified Binary Search

Time Complexity: O(log n)
Space Complexity: O(1)

Date Solved: 05-07-2026
"""
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
        return nums[left]