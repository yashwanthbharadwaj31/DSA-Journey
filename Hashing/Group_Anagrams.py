"""
Problem: Group Anagrams

LeetCode: #49
Difficulty: Medium
Topic: Hashing
Pattern: Hash Map + Sorting

Time Complexity: O(n × k log k)
Space Complexity: O(n × k)

Date Solved: 01-07-2026
"""
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        answer = []
        for value in groups.values():
            answer.append(value)
        return answer