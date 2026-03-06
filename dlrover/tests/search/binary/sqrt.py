"""
给你一个非负整数 x，计算并返回 x的算术平方根。
由于返回类型是整数，结果只保留整数部分，小数部分将被舍去。
注意： 不允许使用任何内置指数函数和算符，例如 pow(x, 0.5)或者 x ** 0.5。


输入: x = 8
输出: 2
解释: 8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
"""

"""
核心思想：
平方根一定在 [0, x]范围内
使用二分查找在这个范围内寻找平方根
注意处理整型溢出
"""


def solve(x: int) -> int:
    if x < 2:
        return x

    left, right = 2, x // 2

    while left <= right:
        mid = left + (right - left) // 2  # 防止溢出
        square = mid * mid

        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1

    return right  # 返回整数部分
