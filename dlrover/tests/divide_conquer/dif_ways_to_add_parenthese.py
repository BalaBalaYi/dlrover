"""给定一个只包含加、减和乘法的数学表达式，求通过加括号可以得到多少种不同的结果。

输入: "2-1-1"
输出: [0, 2]
解释:
((2-1)-1) = 0
(2-(1-1)) = 2

输入: "2 * 3-4 * 5"
输出: [-34, -14, -10, -10, 10]
解释:
(2*(3-(4 * 5))) = -34
((2 * 3)-(4 * 5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2 * 3)-4)*5) = 10

核心：分治法

这是一个典型的分治+记忆化问题。思路是将表达式在每个运算符处分割，递归计算左右两边的所有可能结果，然后根据当前运算符组合结果。

算法步骤：
遍历表达式，遇到运算符时：
递归计算左边表达式的所有可能结果
递归计算右边表达式的所有可能结果
根据当前运算符，组合左右结果
使用记忆化优化重复计算
"""


def solve(expression: str):
    symbols = "+-*"

    def compute(left, right):
        # 如果当前部分是纯数字，直接返回
        if expression[left:right].isdigit():
            return [int(expression[left:right])]

        results = []

        for i in range(left, right):
            if expression[i] in symbols:
                # 递归计算左右两边
                left_results = compute(left, i)
                right_results = compute(i + 1, right)

                # 根据运算符组合结果
                for left_result in left_results:
                    for right_result in right_results:
                        if expression[i] == "+":
                            results.append(left_result + right_result)
                        elif expression[i] == "-":
                            results.append(left_result - right_result)
                        elif expression[i] == "*":
                            results.append(left_result * right_result)
        return results

    return compute(0 , len(expression))



if __name__ == '__main__':
    print(solve("2-1-1"))  # [0, 2]
    print(solve("2*3-4*5"))  # [-34, -14, -10, -10, 10]
