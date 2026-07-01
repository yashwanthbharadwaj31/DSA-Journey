"""
Problem: Valid Parentheses

LeetCode: #20
Difficulty: Easy
Topic: Stack
Pattern: Stack

Time Complexity: O(n)
Space Complexity: O(n)

Date Solved: 01-07-2026
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top != mapping[ch]:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False