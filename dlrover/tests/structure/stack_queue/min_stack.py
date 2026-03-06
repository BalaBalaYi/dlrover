"""设计一个最小栈，除了需要支持常规栈的操作外，还需要支持在O¹1º 时间内查询栈内最小
值的功能。"""


class MinStack:
    def __init__(self):
        """
        初始化栈
        """
        self.stack = []  # 主栈
        self.min_stack = []  # 最小栈

    def push(self, val: int) -> None:
        """
        元素入栈
        时间复杂度: O(1)
        """
        self.stack.append(val)

        # 更新最小栈
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            # 保持最小栈与主栈大小一致
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        """
        元素出栈
        时间复杂度: O(1)
        """
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        """
        获取栈顶元素
        时间复杂度: O(1)
        """
        if self.stack:
            return self.stack[-1]
        return -1  # 根据题目约束，栈非空

    def getMin(self) -> int:
        """
        获取栈中最小元素
        时间复杂度: O(1)
        """
        if self.min_stack:
            return self.min_stack[-1]
        return -1  # 根据题目约束，栈非空


if __name__ == '__main__':
    # 测试
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack.getMin())  # -3
    min_stack.pop()
    print(min_stack.top())  # 0
    print(min_stack.getMin())  # -2