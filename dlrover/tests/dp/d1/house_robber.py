"""假如你是一个劫匪，并且决定抢劫一条街上的房子，每个房子内的钱财数量各不相同。如果
你抢了两栋相邻的房子，则会触发警报机关。求在不触发机关的情况下最多可以抢劫多少钱。

状态定义：
dp[i]表示前 i个房屋能偷到的最大金额
状态转移方程：

对于第 i个房屋（索引从0开始）：
1.偷第 i个房屋：则不能偷第 i-1个房屋
  金额 = dp[i-2] + nums[i]
2.不偷第 i个房屋：
  金额 = dp[i-1]
取两者最大值：dp[i] = max(dp[i-1], dp[i-2] + nums[i])
"""


def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    return dp[-1]


if __name__ == '__main__':
    print(rob([1, 2, 3, 1]))  # 4
    print(rob([2, 7, 9, 3, 1]))  # 12
    print(rob([2, 1, 1, 2]))  # 4
