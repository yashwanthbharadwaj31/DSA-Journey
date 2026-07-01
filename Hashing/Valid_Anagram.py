"""
Problem: Valid Anagram

LeetCode: #242
Difficulty: Easy
Topic: Hashing
Pattern: Frequency Count

Time Complexity: O(n)
Space Complexity: O(1)

Date Solved: 01-07-2026
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False
        return True