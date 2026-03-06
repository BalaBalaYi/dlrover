"""给定一个整数数组，这个数组里只有一个数次出现了一次，其余数字出现了两次，求这个只
出现一次的数字。

核心：异或运算的巧妙应用

异或运算 ^具有以下重要性质：
自反性：a ^ a = 0（相同数异或为0）
与0运算：a ^ 0 = a（任何数与0异或等于自身）
交换律：a ^ b = b ^ a
结合律：(a ^ b) ^ c = a ^ (b ^ c)
关键洞察：
由于数组中只有一个数出现一次，其他数都出现两次
将这些数全部进行异或运算：
出现两次的数：a ^ a = 0
出现一次的数：b ^ 0 = b
最终结果就是只出现一次的那个数

"""


def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


if __name__ == '__main__':
    print(singleNumber([2, 2, 1]))  # 1
    print(singleNumber([4, 1, 2, 1, 2]))  # 4
