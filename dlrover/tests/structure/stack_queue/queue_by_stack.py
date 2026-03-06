"""尝试使用栈（stack）来实现队列（queue）。

输入：
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 1, 1, false]

解释：
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek();  // return 1
myQueue.pop();   // return 1, queue is [2]
myQueue.empty(); // return false
"""


class MyQueue:
    def __init__(self):
        self.stack_in = []  # 输入栈
        self.stack_out = []  # 输出栈

    def push(self, x):
        self.stack_in.append(x)

    def empty(self):
        return not self.stack_in and not self.stack_out

    def _get(self, ret_only=False):
        if self.empty():
            return -1

        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        if ret_only:
            return self.stack_out[-1]
        else:
            return self.stack_out.pop()

    def pop(self):
        return self._get()

    def peek(self):
        return self._get(True)
