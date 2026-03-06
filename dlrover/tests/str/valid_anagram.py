"""判断两个字符串包含的字符是否完全相同。
"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    # 统计字符频率
    count_s = {}
    count_t = {}

    for char in s:
        count_s[char] = count_s.get(char, 0) + 1
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1

    return count_s == count_t