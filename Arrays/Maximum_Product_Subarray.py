"""
Problem: Maximum Product Subarray

LeetCode: #152
Difficulty: Medium
Roadmap Topic: Arrays
GitHub Folder: Arrays
Pattern: Dynamic Tracking

Time Complexity: O(n)
Space Complexity: O(1)

Date Solved: 15-07-2026
"""
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currentMax = nums[0]
        currentMin = nums[0]
        answer = nums[0]
        for num in nums[1:]:
            if num < 0:
                currentMax, currentMin = currentMin, currentMax
            currentMax = max(num, currentMax * num)
            currentMin = min(num, currentMin * num)
            answer = max(answer, currentMax)
        return answer