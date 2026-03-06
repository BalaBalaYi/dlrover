"""给定两个单词 word1和 word2，返回使得 word1和 word2相同所需的最小步数。
每步可以删除任意一个字符串中的一个字符。

输入: word1 = "sea", word2 = "eat"
输出: 2
解释: 第一步将 "sea" 变为 "ea" ，第二步将 "eat" 变为 "ea"

输入: word1 = "leetcode", word2 = "etco"
输出: 4
解释:
- 从 "leetcode" 删除 "l", "d" → "eetcode"
- 从 "etco" 删除 "e" → "tco"
最终都需要删除 4 个字符
"""

"""
状态定义：
dp[i][j]：使 word1的前 i 个字符和 word2的前 j 个字符相同所需的最小删除操作数

状态转移：
1. 如果 word1[i-1] == word2[j-1]:
dp[i][j] = dp[i-1][j-1]
2. 如果 word1[i-1] != word2[j-1]:
// 1. 删除word1: dp[i-1][j]+1
// 2. 删除word2：dp[i][j-1]+1
dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1))

初始化：
dp[0][j]=j: 删除所有word2的字符
dp[i][0]=i: 删除所有word1的字符
"""


def solve(word1, word2):
    if not word1 and not word2:
        return 0

    m = len(word1)
    n = len(word2)

    # 初始化
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j]+1, dp[i][j - 1]+1)

    return dp[m][n]


if __name__=="__main__":
    print(solve(word1="sea", word2="eat"))  # 2

