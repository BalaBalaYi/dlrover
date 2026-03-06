"""给定两个字符串 text1和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在公共子序列，返回 0。
一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，它的长度为 3。

输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。

输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0。
"""

"""
dp[i][j]:
text1的前i个字符和text2的前j个字符的最长公共子序列长度。
注意：这里的 i和 j表示字符个数，不是索引。dp[i][j]对应 text1[0:i-1]和 text2[0:j-1]。

1. 如果 text1[i-1] == text2[j-1]（最后一个字符相同）：
这个字符一定在公共子序列中
dp[i][j] = dp[i-1][j-1] + 1

2. 如果 text1[i-1] != text2[j-1]（最后一个字符不同）：
最后一个字符不可能同时在公共子序列中
我们需要考虑两种选择的最大值：
不使用 text1[i-1]：dp[i-1][j]
不使用 text2[j-1]：dp[i][j-1]
dp[i][j] = max(dp[i-1][j], dp[i][j-1])
"""


def longest_common_subseq(text1, text2):
    m = len(text1)
    n = len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]
