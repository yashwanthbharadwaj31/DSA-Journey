from collections import Counter
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        frequencies = Counter(tasks).values()
        max_freq = max(frequencies)
        max_count = sum(
            freq == max_freq for freq in Counter(tasks).values()
        )

        intervals = (max_freq - 1) * (n + 1) + max_count
        return max(len(tasks), intervals)
