from collections import Counter
class Solution:
    def minWindow(self, s, t):
        if not s or not t or len(t) > len(s):
            return ""
        need = Counter(t)
        missing = len(t)
        left = 0
        start = 0
        min_length = float('inf')
        for right, char in enumerate(s):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            while missing == 0:
                window_length = right - left + 1
                if window_length < min_length:
                    min_length = window_length
                    start = left
                left_char = s[left]
                need[left_char] += 1
                if need[left_char] > 0:
                    missing += 1
                left += 1
        if min_length == float('inf'):
            return ""
        return s[start:start + min_length]
