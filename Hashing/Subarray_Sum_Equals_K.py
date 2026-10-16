class Solution:
    def subarraySum(self, nums, k):
        prefix_sum = 0
        count = 0
        prefix_counts = {0: 1}
        for num in nums:
            prefix_sum += num
            needed = prefix_sum - k
            count += prefix_counts.get(needed, 0)
            prefix_counts[prefix_sum] = (
                prefix_counts.get(prefix_sum, 0) + 1
            )
        return count
