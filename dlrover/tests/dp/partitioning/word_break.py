"""
给你一个字符串 s和一个字符串列表 wordDict作为字典。如果可以利用字典中出现的单词拼接出 s，则返回 true；否则，返回 false。
注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。
"""
from typing import List

"""
核心思路:

这是一个典型的字符串分割问题。我们可以将问题转化为：
判断字符串 s是否能被分割成若干个子串，每个子串都在字典中。

状态定义:
定义 dp[i]表示：字符串 s的前 i个字符（即 s[0...i-1]）能否被字典中的单词完全拆分。
dp[0] = true：空字符串可以被拆分（即不选任何单词）。
最终答案：dp[n]，其中 n = len(s)。

状态转移方程:
对于每个位置 i（从 1到 n）：
我们枚举所有可能的分割点 j（0 ≤ j < i），检查：
1.前 j个字符能否被拆分（即 dp[j] == true）
2.子串 s[j:i]是否在字典中
dp[i] = any(dp[j] and s[j:i] in wordDict for j in range(i))

"""


def solve(s: str, word_dict: List[str]) -> bool:
    n = len(s)
    dp = [False] * (n + 1)
    word_set = set(word_dict)

    dp[0] = True
    for i in range(1, n + 1):
        for j in range(1, i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]
