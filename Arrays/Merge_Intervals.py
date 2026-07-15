"""
Problem: Merge Intervals

LeetCode: #56
Difficulty: Medium
Roadmap Topic: Arrays
GitHub Folder: Arrays
Pattern: Sorting + Interval Merging

Time Complexity: O(n log n)
Space Complexity: O(n)

Date Solved: 15-07-2026
"""
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged