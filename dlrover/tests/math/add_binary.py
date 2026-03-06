"""Add Binary

输入: a = "11", b = "1"
输出: "100"
解释: 11₂ + 1₂ = 100₂
"""


def addBinary(a: str, b: str) -> str:
    """
    双指针模拟竖式加法
    时间复杂度: O(max(m, n))
    空间复杂度: O(max(m, n))
    """
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        # 获取当前位的数字
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0

        # 计算当前位的和
        total = digit_a + digit_b + carry

        # 计算当前位的值和进位
        # 二进制：和 mod 2 得到当前位，整除 2 得到进位
        current_digit = total % 2
        carry = total // 2

        # 添加到结果
        result.append(str(current_digit))

        # 移动指针
        i -= 1
        j -= 1

    # 反转结果（因为是从最低位开始加的）
    return ''.join(result[::-1])


# 测试
print(addBinary("11", "1"))  # "100"
print(addBinary("1010", "1011"))  # "10101"
print(addBinary("0", "0"))  # "0"
