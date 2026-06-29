"""
Problem: Longest Palindromic Substring

LeetCode: #5
Difficulty: Medium
Topic: Strings
Pattern: Expand Around Center

Time Complexity: O(n²)
Space Complexity: O(1)

Date Solved: 30-06-2026
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            # Odd length palindrome
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(longest):
                    longest = s[left:right + 1]
                left -= 1
                right += 1
            # Even length palindrome
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(longest):
                    longest = s[left:right + 1]
                left -= 1
                right += 1
        return longest