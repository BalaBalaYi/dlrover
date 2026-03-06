"""Longest Substring Without Repeating Characters

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以长度为 3。
"""


def solve(s: str):
    if not s:
        return 0

    if len(s) == 1:
        return 1

    l, r = 0, 0
    num_window = set()
    max_length = 0

    for char in s:
        # 如果不重复，则窗口结束右移
        if char not in num_window:
            pass
        else:
            # 如果重复，移除淘汰的字符,窗口起始右移
            l_value = s[l]
            num_window.remove(l_value)
            l += 1
        r += 1
        num_window.add(char)
        max_length = max(r - l + 1, max_length)

    return r - l


if __name__ == '__main__':
    print(solve("abcabcbb"))  # 3
    print(solve("bbbbb"))  # 1
