"""
Problem: Best Time to Buy and Sell Stock

LeetCode: #121
Difficulty: Easy
Roadmap Topic: Arrays
GitHub Folder: Arrays
Pattern: Greedy

Time Complexity: O(n)
Space Complexity: O(1)

Date Solved: 13-07-2026
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimumPrice = prices[0]
        maximumProfit = 0
        for currentPrice in prices[1:]:
            minimumPrice = min(minimumPrice, currentPrice)
            currentProfit = currentPrice - minimumPrice
            maximumProfit = max(maximumProfit, currentProfit)
        return maximumProfit