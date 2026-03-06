"""给定一个包含加减乘除整数运算的字符串，求其运算结果，只保留整数。"

输入: s = "3+2 * 2"
输出: 7
"""

def calculate(s: str) -> int:
    stack = []
    num = 0
    sign = "+"

    for i, char in enumerate(s):
        # 如果是数字
        if char.isdigit():
            num = num * 10 + int(char)

        # 如果是非数字（操作符）
        if not char.isdigit() and char != ' ' or i == len(s) - 1:
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(num * -1)
            elif sign == "*":
                stack[-1] = num * stack[-1]
            elif sign == "/":
                stack[-1] = stack[-1] // num

            num = 0
            sign = char

    return sum(stack)


if __name__ == '__main__':
    # print(calculate("3+2 * 2"))  # 7
    print(calculate(" 3/2 "))  # 1
    print(calculate(" 3+5 / 2 "))  # 5
    print(calculate("1-1+1"))  # 1
