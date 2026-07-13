"""
Problem: Contains Duplicate

LeetCode: #217
Difficulty: Easy
Roadmap Topic: Arrays
GitHub Folder: Arrays
Pattern: Hash Set

Time Complexity: O(n)
Space Complexity: O(n)

Date Solved: 13-07-2026
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False