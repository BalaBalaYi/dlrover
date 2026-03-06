"""你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，
这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组 nums，计算你在不触动警报装置的情况下，今晚能够偷窃到的最高金额。

输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4。
"""


def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])

    n = len(nums)

    # 辅助函数：解决线性打家劫舍问题
    def rob_linear(nums_subarray):
        m = len(nums_subarray)
        if m == 0:
            return 0
        if m == 1:
            return nums_subarray[0]

        # 创建 DP 数组
        dp = [0] * (m + 1)

        # 初始化
        dp[0] = 0  # 没有房屋
        dp[1] = nums_subarray[0]  # 只有第一间房屋

        # 状态转移
        for i in range(2, m + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums_subarray[i - 1])

        return dp[m]

    # 情况1：不偷最后一间房屋（考虑 nums[0] 到 nums[n-2]）
    case1 = rob_linear(nums[0:n - 1])

    # 情况2：不偷第一间房屋（考虑 nums[1] 到 nums[n-1]）
    case2 = rob_linear(nums[1:n])

    return max(case1, case2)


if __name__ == '__main__':
    print(rob([2, 3, 2]))  # 3
    print(rob([1, 2, 3, 1]))  # 4
