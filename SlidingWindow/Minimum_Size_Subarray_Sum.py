class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        window_sum = 0
        min_length = len(nums) + 1
        for right, num in enumerate(nums):
            window_sum += num
            while window_sum >= target:
                min_length = min(min_length, right - left + 1)
                window_sum -= nums[left]
                left += 1
        return 0 if min_length == len(nums) + 1 else min_length
