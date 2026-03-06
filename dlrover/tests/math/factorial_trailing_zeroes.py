"""给定一个非负整数，判断它的阶乘结果的结尾有几个0。


以 n = 100 为例：
第一轮：n = 100，count += 20（100 以内有 20 个 5 的倍数）。
第二轮：n = 20，count += 4（100 以内有 4 个 25 的倍数）。
第三轮：n = 4，count += 0（100 以内没有 125 的倍数）。
最终结果：20 + 4 = 24。

"""

def trailingZeroes(n: int) -> int:
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count
