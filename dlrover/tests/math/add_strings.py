"""给定两个由数字组成的字符串，求它们相加的结果。

输入: num1 = "456", num2 = "77"
输出: "533"
"""


def addStrings(str1, str2):
    i = len(str1) - 1
    j = len(str2) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry > 0:
        digit1  = int(str1[i]) if i >= 0 else 0
        digit2 = int(str2[j]) if j >= 0 else 0

        total = digit1 + digit2 + carry
        current_digit = total % 10
        carry = total // 10
        result.append(str(current_digit))

        i -= 1
        j -= 1

    return ''.join(result[::-1])


if __name__ == '__main__':
    print(addStrings("11", "123"))  # "134"
    print(addStrings("456", "77"))  # "533"
    print(addStrings("0", "0"))  # "0"
