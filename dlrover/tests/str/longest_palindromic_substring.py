"""Longest Palindromic Substring

输入: "babad"
输出: "bab"
解释: "aba" 也是一个有效答案。
"""


def solve(s: str) -> str:
    result = ""
    if not s:
        return result

    if len(s) == 1:
        return s

    def cal_by_mid(l, r):

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        # 循环退出时是不匹配的状态
        return s[l+1:r]

    for i, _ in enumerate(s):
        tmp_0 = cal_by_mid(i, i)
        tmp_1 = cal_by_mid(i, i + 1)
        if len(tmp_0) > len(result):
            result = tmp_0
        if len(tmp_1) > len(result):
            result = tmp_1

    return result


if __name__ == '__main__':
    print(solve("babad"))  # bab
    print(solve("cbbd"))  # bb
