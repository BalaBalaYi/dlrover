"""给定一个0-1 字符串，求有多少非空子字符串的0 和1 数量相同。"""


def count_binary_substrings(s: str) -> int:
    count = {0: 1}  # 前缀和 0 出现 1 次（空串）
    cur = 0
    ans = 0
    for ch in s:
        cur += 1 if ch == '1' else -1
        if cur in count:
            ans += count[cur]
        count[cur] = count.get(cur, 0) + 1
    return ans


if __name__ == '__main__':
    # 示例
    print(count_binary_substrings("0101"))  # 输出 4
    # print(count_binary_substrings("0011"))  # 输出 2
    # print(count_binary_substrings("1010"))  # 输出 4