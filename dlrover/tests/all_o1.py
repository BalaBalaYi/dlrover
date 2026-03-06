"""
设计一个数据结构，支持以下操作：
inc(key) - 将指定 key 的计数增加 1。如果 key 不存在，则插入 key 并设置计数为 1。
dec(key) - 将指定 key 的计数减少 1。如果 key 的计数减少到 0，则从数据结构中删除 key。
getMaxKey() - 返回计数最大的任意一个 key。如果数据结构为空，返回空字符串 ""。
getMinKey() - 返回计数最小的任意一个 key。如果数据结构为空，返回空字符串 ""。
要求：所有操作的平均时间复杂度为 O(1)。

"""


class Node:
    """双向链表节点，代表一个频率桶"""

    def __init__(self, freq=0):
        self.freq = freq  # 当前桶的频率值
        self.keys = set()  # 具有该频率的所有key
        self.prev = None  # 前驱节点
        self.next = None  # 后继节点

    def __repr__(self):
        return f"Node(freq={self.freq}, keys={self.keys})"


class AllOne:
    """
    全O(1)数据结构实现
    支持inc, dec, getMaxKey, getMinKey全部O(1)时间复杂度
    """

    def __init__(self):
        """初始化数据结构"""
        # 哈希表：key -> 所在节点
        self.key_to_node = {}

        # 双向链表：头尾哨兵节点
        self.head = Node()  # 头节点，频率最低（辅助节点）
        self.tail = Node()  # 尾节点，频率最高（辅助节点）
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        """
        增加key的计数

        Args:
            key: 要增加计数的键
        """
        if key not in self.key_to_node:
            # key不存在，插入到频率为1的桶中
            self._add_key_to_freq(key, 1)
        else:
            # key已存在，移动到频率+1的桶中
            current_node = self.key_to_node[key]
            current_freq = current_node.freq
            self._move_key_to_freq(key, current_node, current_freq + 1)

    def dec(self, key: str) -> None:
        """
        减少key的计数

        Args:
            key: 要减少计数的键

        Note:
            如果计数减到0，则删除key
        """
        if key not in self.key_to_node:
            return

        current_node = self.key_to_node[key]
        current_freq = current_node.freq

        if current_freq == 1:
            # 频率减到0，删除key
            self._remove_key(key, current_node)
        else:
            # 移动到频率-1的桶中
            self._move_key_to_freq(key, current_node, current_freq - 1)

    def getMaxKey(self) -> str:
        """
        获取计数最大的任意一个key

        Returns:
            计数最大的key，如果为空则返回""
        """
        if self.head.next == self.tail:
            return ""

        # 尾节点的前一个节点是频率最高的桶
        max_node = self.tail.prev
        return next(iter(max_node.keys))

    def getMinKey(self) -> str:
        """
        获取计数最小的任意一个key

        Returns:
            计数最小的key，如果为空则返回""
        """
        if self.head.next == self.tail:
            return ""

        # 头节点的后一个节点是频率最低的桶
        min_node = self.head.next
        return next(iter(min_node.keys))

    def _add_key_to_freq(self, key: str, freq: int) -> None:
        """
        将key添加到指定频率的桶中

        Args:
            key: 要添加的键
            freq: 目标频率
        """
        # 找到应该插入的位置（在第一个freq >= 目标freq的节点之前）
        current = self.head.next
        while current != self.tail and current.freq < freq:
            current = current.next

        if current != self.tail and current.freq == freq:
            # 已存在该频率的桶，直接添加到keys集合中
            target_node = current
        else:
            # 需要创建新的频率桶
            target_node = Node(freq)
            self._insert_node_before(target_node, current)

        # 添加key到桶中，并更新映射
        target_node.keys.add(key)
        self.key_to_node[key] = target_node

    def _move_key_to_freq(self, key: str, from_node: Node,
                          to_freq: int) -> None:
        """
        将key从一个频率桶移动到另一个频率桶

        Args:
            key: 要移动的键
            from_node: 当前所在的节点
            to_freq: 目标频率
        """
        # 从原节点中移除key
        from_node.keys.remove(key)

        # 找到目标节点（应该在from_node的哪个方向？）
        if to_freq > from_node.freq:
            # 频率增加，向右找
            target = from_node.next
            while target != self.tail and target.freq < to_freq:
                target = target.next
        else:
            # 频率减少，向左找
            target = from_node.prev
            while target != self.head and target.freq > to_freq:
                target = target.prev

        # 检查目标频率节点是否存在
        if (target != self.head and target != self.tail and
                target.freq == to_freq):
            # 目标节点已存在
            to_node = target
        else:
            # 需要创建新节点
            to_node = Node(to_freq)
            if to_freq > from_node.freq:
                self._insert_node_before(to_node, target)
            else:
                self._insert_node_after(to_node, target)

        # 将key添加到新节点
        to_node.keys.add(key)
        self.key_to_node[key] = to_node

        # 如果原节点为空，则删除
        if not from_node.keys:
            self._remove_node(from_node)

    def _remove_key(self, key: str, node: Node) -> None:
        """
        从数据结构中删除key

        Args:
            key: 要删除的键
            node: key所在的节点
        """
        # 从节点中移除key
        node.keys.remove(key)

        # 从哈希表中删除映射
        del self.key_to_node[key]

        # 如果节点为空，则删除节点
        if not node.keys:
            self._remove_node(node)

    def _insert_node_before(self, new_node: Node, target: Node) -> None:
        """
        在目标节点之前插入新节点

        Args:
            new_node: 要插入的新节点
            target: 目标节点
        """
        prev_node = target.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = target
        target.prev = new_node

    def _insert_node_after(self, new_node: Node, target: Node) -> None:
        """
        在目标节点之后插入新节点

        Args:
            new_node: 要插入的新节点
            target: 目标节点
        """
        next_node = target.next
        target.next = new_node
        new_node.prev = target
        new_node.next = next_node
        next_node.prev = new_node

    def _remove_node(self, node: Node) -> None:
        """
        从链表中删除节点

        Args:
            node: 要删除的节点
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def display(self) -> None:
        """打印数据结构当前状态"""
        print("AllOne数据结构状态:")
        print(f"  总key数量: {len(self.key_to_node)}")

        # 遍历链表
        current = self.head.next
        while current != self.tail:
            print(f"  频率 {current.freq}: {current.keys}")
            current = current.next

        if self.head.next == self.tail:
            print("  数据结构为空")
        else:
            print(f"  最小key: {self.getMinKey()}")
            print(f"  最大key: {self.getMaxKey()}")
        print("-" * 40)


# ========== 简化版本（面试友好） ==========
class AllOneSimple:
    """
    简化版本，更易理解和实现
    """

    def __init__(self):
        # 存储每个key的计数
        self.count = {}
        # 按频率分组的桶
        self.freq_buckets = {}
        # 当前最小频率和最大频率
        self.min_freq = 0
        self.max_freq = 0

    def inc(self, key: str) -> None:
        # 获取当前计数
        current_count = self.count.get(key, 0)

        # 更新计数
        new_count = current_count + 1
        self.count[key] = new_count

        # 从旧桶中移除
        if current_count > 0:
            self.freq_buckets[current_count].remove(key)
            if not self.freq_buckets[current_count]:
                del self.freq_buckets[current_count]
                if self.min_freq == current_count:
                    self.min_freq += 1

        # 添加到新桶
        if new_count not in self.freq_buckets:
            self.freq_buckets[new_count] = set()
        self.freq_buckets[new_count].add(key)

        # 更新最大频率
        self.max_freq = max(self.max_freq, new_count)

        # 更新最小频率
        if new_count == 1:
            self.min_freq = 1
        elif key in self.freq_buckets.get(self.min_freq, set()):
            # 如果最小频率桶不为空，则最小频率不变
            pass
        else:
            # 需要重新计算最小频率
            self.min_freq += 1

    def dec(self, key: str) -> None:
        if key not in self.count:
            return

        current_count = self.count[key]

        if current_count == 1:
            # 删除key
            del self.count[key]
            self.freq_buckets[1].remove(key)
            if not self.freq_buckets[1]:
                del self.freq_buckets[1]
        else:
            # 减少计数
            new_count = current_count - 1
            self.count[key] = new_count

            # 从旧桶中移除
            self.freq_buckets[current_count].remove(key)
            if not self.freq_buckets[current_count]:
                del self.freq_buckets[current_count]
                if self.max_freq == current_count:
                    self.max_freq -= 1

            # 添加到新桶
            if new_count not in self.freq_buckets:
                self.freq_buckets[new_count] = set()
            self.freq_buckets[new_count].add(key)

        # 更新最小频率
        if not self.count:
            self.min_freq = 0
            self.max_freq = 0
        else:
            # 重新计算最小频率
            while self.min_freq not in self.freq_buckets:
                self.min_freq += 1

    def getMaxKey(self) -> str:
        if not self.count:
            return ""

        # 从最大频率桶中取任意一个key
        return next(iter(self.freq_buckets[self.max_freq]))

    def getMinKey(self) -> str:
        if not self.count:
            return ""

        # 从最小频率桶中取任意一个key
        return next(iter(self.freq_buckets[self.min_freq]))

    def display(self):
        print(f"AllOneSimple状态:")
        print(f"  计数: {self.count}")
        print(f"  频率桶: {self.freq_buckets}")
        print(f"  min_freq: {self.min_freq}, max_freq: {self.max_freq}")
        print(
            f"  getMinKey: {self.getMinKey()}, getMaxKey: {self.getMaxKey()}")
        print("-" * 40)


# ========== 测试用例 ==========
def test_all_one():
    """测试AllOne数据结构"""
    print("=" * 60)
    print("测试 All O`one Data Structure")
    print("=" * 60)

    # 测试完整版本
    print("测试完整版本:")
    all_one = AllOne()

    # 测试用例1: 基本功能
    print("\n1. 基本功能测试:")
    all_one.inc("apple")
    all_one.inc("apple")
    all_one.inc("banana")
    all_one.display()

    print(f"getMaxKey: {all_one.getMaxKey()}")  # 应该返回"apple"
    print(f"getMinKey: {all_one.getMinKey()}")  # 应该返回"banana"

    # 测试用例2: 增加和减少
    print("\n2. 增加和减少测试:")
    all_one.inc("banana")
    all_one.inc("banana")
    all_one.display()  # apple:2, banana:3

    all_one.dec("apple")
    all_one.display()  # apple:1, banana:3

    all_one.dec("apple")
    all_one.display()  # banana:3 (apple被删除)

    print(f"getMaxKey: {all_one.getMaxKey()}")  # 应该返回"banana"
    print(f"getMinKey: {all_one.getMinKey()}")  # 应该返回"banana"

    # 测试用例3: 多个key
    print("\n3. 多个key测试:")
    all_one.inc("cherry")
    all_one.inc("cherry")
    all_one.inc("cherry")
    all_one.inc("date")
    all_one.display()  # banana:3, cherry:3, date:1

    print(f"getMaxKey: {all_one.getMaxKey()}")  # 可能返回"banana"或"cherry"
    print(f"getMinKey: {all_one.getMinKey()}")  # 应该返回"date"

    # 测试用例4: 边界条件
    print("\n4. 边界条件测试:")
    all_one.dec("date")
    all_one.display()  # date被删除

    # 空数据结构测试
    all_one.dec("banana")
    all_one.dec("banana")
    all_one.dec("banana")
    all_one.dec("cherry")
    all_one.dec("cherry")
    all_one.dec("cherry")
    all_one.display()  # 应该为空

    print(f"空时getMaxKey: '{all_one.getMaxKey()}'")  # 应该返回""
    print(f"空时getMinKey: '{all_one.getMinKey()}'")  # 应该返回""


def test_all_one_simple():
    """测试简化版本"""
    print("\n\n测试简化版本:")
    all_one = AllOneSimple()

    # 测试基本功能
    all_one.inc("apple")
    all_one.inc("apple")
    all_one.inc("banana")
    all_one.display()

    all_one.inc("banana")
    all_one.inc("banana")
    all_one.display()

    all_one.dec("apple")
    all_one.display()

    all_one.dec("apple")
    all_one.display()

    print(f"getMaxKey: {all_one.getMaxKey()}")
    print(f"getMinKey: {all_one.getMinKey()}")


def test_performance():
    """性能测试"""
    print("\n\n性能测试:")
    import time

    all_one = AllOne()

    # 插入大量key
    start = time.time()
    for i in range(10000):
        all_one.inc(f"key_{i}")
        all_one.inc(f"key_{i}")  # 每个key增加两次

    insert_time = time.time() - start
    print(f"插入20000次操作耗时: {insert_time:.4f}秒")

    # 随机访问最大最小key
    start = time.time()
    for _ in range(10000):
        max_key = all_one.getMaxKey()
        min_key = all_one.getMinKey()

    query_time = time.time() - start
    print(f"查询20000次最大最小key耗时: {query_time:.4f}秒")

    # 混合操作
    start = time.time()
    for i in range(5000):
        all_one.inc(f"key_{i % 100}")
        all_one.dec(f"key_{(i + 50) % 100}")

    mix_time = time.time() - start
    print(f"混合操作10000次耗时: {mix_time:.4f}秒")


# ========== 实际应用示例 ==========
class HotKeywordTracker:
    """
    实际应用：热点关键词追踪系统
    """

    def __init__(self):
        self.all_one = AllOne()
        self.keyword_history = {}

    def track_search(self, keyword: str) -> None:
        """追踪搜索关键词"""
        self.all_one.inc(keyword)

        # 记录搜索时间
        import datetime
        if keyword not in self.keyword_history:
            self.keyword_history[keyword] = []
        self.keyword_history[keyword].append(datetime.datetime.now())

    def get_hot_keywords(self, top_n: int = 10) -> list:
        """获取热点关键词"""
        # 这里简化实现，实际应该能返回top_n个
        max_key = self.all_one.getMaxKey()
        return [max_key] if max_key else []

    def get_trending_keywords(self) -> list:
        """获取新兴关键词（频率较低但有增长潜力）"""
        min_key = self.all_one.getMinKey()
        return [min_key] if min_key else []

    def get_keyword_stats(self, keyword: str) -> dict:
        """获取关键词统计信息"""
        if keyword not in self.keyword_history:
            return {"count": 0, "first_seen": None, "last_seen": None}

        times = self.keyword_history[keyword]
        return {
            "count": len(times),
            "first_seen": min(times) if times else None,
            "last_seen": max(times) if times else None
        }

    def display_dashboard(self):
        """显示监控面板"""
        print("\n热点关键词监控面板:")
        print(f"当前最热门: {self.all_one.getMaxKey()}")
        print(f"当前新兴词: {self.all_one.getMinKey()}")
        print("-" * 40)


# ========== 主程序 ==========
if __name__ == "__main__":
    # 运行测试
    test_all_one()
    test_all_one_simple()
    test_performance()

    # 演示实际应用
    print("\n" + "=" * 60)
    print("实际应用：热点关键词追踪系统")
    print("=" * 60)

    tracker = HotKeywordTracker()

    # 模拟搜索数据
    searches = [
        "python", "python", "python", "java", "java",
        "javascript", "python", "go", "rust", "python",
        "java", "javascript", "python", "typescript"
    ]

    for keyword in searches:
        tracker.track_search(keyword)

    tracker.display_dashboard()

    # 查看具体关键词统计
    print("\n关键词统计:")
    for keyword in ["python", "java", "rust"]:
        stats = tracker.get_keyword_stats(keyword)
        print(f"{keyword}: 搜索{stats['count']}次")

    print("\n所有测试完成！")