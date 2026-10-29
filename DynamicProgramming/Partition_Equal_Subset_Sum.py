class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = bytearray(target + 1)
        dp[0] = 1
        for num in nums:
            for s in range(target, num - 1, -1):
                if dp[s - num]:
                    dp[s] = 1
            if dp[target]:
                return True
        return bool(dp[target])
