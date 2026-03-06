"""给定一个十进制整数，求它在七进制下的表示。

输入: num = 100
输出: "202"
解释: 100 的 7 进制是 2×7² + 0×7¹ + 2×7⁰ = 202

核心：除基取余法

将一个十进制数转换为 N 进制的基本方法是除基取余，逆序排列：
用 N 去除十进制数，得到商和余数
记录余数（0 ≤ 余数 < N）
用商继续除以 N，重复直到商为 0
将记录的余数逆序排列，得到 N 进制表示
特殊处理：
负数：先转换绝对值，最后加负号
0：直接返回 "0"

"""
from string import digits


def solve(num):
    if num == 0:
        return "0"

    if num < 0:
        negative = True
    else:
        negative = False
    num = abs(num)

    digits = []

    while num > 0:
        reminder = num % 7
        digits.append(str(reminder))
        num //= 7

    result = "".join(reversed(digits))

    if negative:
        result = "-" + result

    return result


if __name__ == '__main__':
    print(solve(100))  # 202
    print(solve(-7))  # -10
