from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        frequency = Counter(nums)
        heap = []
        for num, count in frequency.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for count, num in heap]
