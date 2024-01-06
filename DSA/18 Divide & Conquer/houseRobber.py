def rob(n):
    if len(n) == 0:
        return 0
    for i in range(len(n)):
        first = n[i] + rob(n[i+2:])
        second = rob(n[i+1:])
        return max(first, second)


def rob_DP(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    return dp[-1]


# Example usage
# print(rob_DP([6, 9, 3, 1, 2, 4]))  # Output: 4


houses = [6, 7, 1, 30, 8, 2]
print(rob(houses))
