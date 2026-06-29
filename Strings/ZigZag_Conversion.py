"""
Problem: Zigzag Conversion

LeetCode: #6
Difficulty: Medium
Topic: Strings
Pattern: Simulation

Time Complexity: O(n)
Space Complexity: O(n)

Date Solved: 30-06-2026
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = []
        for i in range(numRows):
            rows.append("")
        currentRow = 0
        goingDown = True
        for ch in s:
            rows[currentRow] += ch
            if currentRow == 0:
                goingDown = True
            elif currentRow == numRows - 1:
                goingDown = False
            if goingDown:
                currentRow += 1
            else:
                currentRow -= 1
        answer = ""
        for row in rows:
            answer += row
        return answer