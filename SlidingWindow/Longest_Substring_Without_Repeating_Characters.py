"""
Problem: Longest Substring Without Repeating Characters

LeetCode: #3
Difficulty: Medium
Topic: Sliding Window

Time Complexity: O(n)
Space Complexity: O(min(n, m))

Date Solved: 29-06-2026
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_length = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left = left + 1
            seen.add(s[right])
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
        return max_length        