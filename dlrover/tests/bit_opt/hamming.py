"""给定两个十进制数字，求它们二进制表示的汉明距离（Hamming distance，即不同位的个数）。

输入: x = 1, y = 4
输出: 2
解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
不同的位用 ↑ 标出
"""


def hammingDistance(x: int, y: int) -> int:
    """
    逐位比较
    时间复杂度: O(32) = O(1)
    空间复杂度: O(1)
    """

    return bin(x ^ y).count('1')


def hammingDistance_bit(x: int, y: int) -> int:
    """
    位运算统计1的个数
    时间复杂度: O(k)，k是二进制位数
    空间复杂度: O(1)
    """
    xor = x ^ y
    distance = 0

    # 统计 xor 中1的个数
    while xor:
        distance += 1
        xor = xor & (xor - 1)  # 清除最低位的1

    return distance


if __name__ == '__main__':
    print(hammingDistance(1, 4))  # 2
    print(hammingDistance_bit(3, 1))  # 1
