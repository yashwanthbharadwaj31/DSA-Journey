"""
Problem: Product of Array Except Self

LeetCode: #238
Difficulty: Medium
Roadmap Topic: Arrays
GitHub Folder: Arrays
Pattern: Prefix Product + Suffix Product

Time Complexity: O(n)
Space Complexity: O(1) (excluding output array)

Date Solved: 14-07-2026
"""
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer