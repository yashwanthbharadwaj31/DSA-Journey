"""
Problem: Maximum Subarray

LeetCode: #53
Difficulty: Medium
Roadmap Topic: Arrays
GitHub Folder: Arrays
Pattern: Kadane's Algorithm

Time Complexity: O(n)
Space Complexity: O(1)

Date Solved: 14-07-2026
"""
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = nums[0]
        maximumSum = nums[0]
        for num in nums[1:]:
            currentSum = max(num, currentSum + num)
            maximumSum = max(maximumSum, currentSum)
        return maximumSum