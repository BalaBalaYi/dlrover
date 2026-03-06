"""给定每天的温度，求对于每一天需要等几天才可以等到更暖和的一天。如果该天之后不存在
更暖和的天气，则记为0。"""



def dailyTemperatures(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    n = len(temperatures)
    result = [0] * n  # 初始化结果数组，默认值为0
    stack = []  # 栈，存储索引

    for i in range(n):
        # 当栈不为空且当前温度大于栈顶索引对应的温度
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()  # 弹出栈顶索引
            result[prev_index] = i - prev_index  # 计算天数差
        # 将当前索引入栈
        stack.append(i)

    return result


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(dailyTemperatures(temperatures))  # [1, 1, 4, 2, 1, 1, 0, 0]
