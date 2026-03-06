class MaxHeap:
    def __init__(self, capacity=10):
        """
        初始化最大堆
        capacity: 初始容量
        """
        self.heap = [0] * capacity
        self.size = 0
        self.capacity = capacity

    def _parent(self, index):
        """返回父节点索引"""
        return (index - 1) // 2

    def _left_child(self, index):
        """返回左子节点索引"""
        return 2 * index + 1

    def _right_child(self, index):
        """返回右子节点索引"""
        return 2 * index + 2

    def _swap(self, i, j):
        """交换两个位置的值"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, index):
        """向上堆化（插入时使用）"""
        while index > 0 and self.heap[self._parent(index)] < self.heap[index]:
            self._swap(index, self._parent(index))
            index = self._parent(index)

    def _heapify_down(self, index):
        """向下堆化（删除最大值时使用）"""
        max_index = index

        while True:
            left = self._left_child(index)
            right = self._right_child(index)

            # 找出当前节点、左子节点、右子节点中的最大值
            if left < self.size and self.heap[left] > self.heap[max_index]:
                max_index = left

            if right < self.size and self.heap[right] > self.heap[max_index]:
                max_index = right

            # 如果当前节点已经是最大值，停止
            if max_index == index:
                break

            # 否则，交换并继续向下堆化
            self._swap(index, max_index)
            index = max_index

    def _resize(self):
        """扩容"""
        new_capacity = self.capacity * 2
        new_heap = [0] * new_capacity

        for i in range(self.size):
            new_heap[i] = self.heap[i]

        self.heap = new_heap
        self.capacity = new_capacity

    def insert(self, value):
        """
        插入元素
        时间复杂度: O(log n)
        """
        if self.size == self.capacity:
            self._resize()

        # 将新元素放在末尾
        self.heap[self.size] = value
        self.size += 1

        # 向上堆化
        self._heapify_up(self.size - 1)

    def extract_max(self):
        """
        删除并返回最大值
        时间复杂度: O(log n)
        """
        if self.size == 0:
            raise IndexError("Heap is empty")

        # 保存最大值
        max_value = self.heap[0]

        # 将最后一个元素移到根节点
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1

        # 向下堆化
        self._heapify_down(0)

        return max_value

    def get_max(self):
        """
        返回最大值但不删除
        时间复杂度: O(1)
        """
        if self.size == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def is_empty(self):
        """判断堆是否为空"""
        return self.size == 0

    def __len__(self):
        """返回堆的大小"""
        return self.size

    def __str__(self):
        """字符串表示"""
        return str(self.heap[:self.size])


# 测试
if __name__ == "__main__":
    heap = MaxHeap()

    # 插入元素
    heap.insert(10)
    heap.insert(20)
    heap.insert(5)
    heap.insert(30)
    heap.insert(15)

    print("当前堆:", heap)  # [30, 20, 5, 10, 15]
    print("最大值:", heap.get_max())  # 30

    # 删除最大值
    print("删除最大值:", heap.extract_max())  # 30
    print("删除后堆:", heap)  # [20, 15, 5, 10]
    print("新的最大值:", heap.get_max())  # 20