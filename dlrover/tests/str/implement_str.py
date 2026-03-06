"""判断一个字符串是不是另一个字符串的子字符串，并返回其位置。

输入：s = "hello world", t = "world"
输出：6

输入：s = "apple", t = "banana"
输出：-1
"""

def solve(s, t):
    m = len(s)
    n = len(t)

    if n == 0:
        return 0
    if m < n:
        return -1

    i = 0
    while i <= m -n:
        if s[i] == t[0]:
            match = True
            for j in range(1, n):
                if s[i + j] != t[j]:
                    match = False
                    break
            if match:
                return i
        i += 1
    return -1

if __name__ == '__main__':
    print(solve("hello world", "world"))  # 6

