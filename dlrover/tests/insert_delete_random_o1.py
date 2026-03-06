"""
支持在 O(1) 平均时间复杂度内完成插入、删除和获取随机元素的数据结构。
"""

import random


class RandomizedSet:
    """
    支持O(1)时间插入、删除和获取随机元素的数据结构
    LeetCode 380: Insert Delete GetRandom O(1)
    """

    def __init__(self):
        """初始化数据结构"""
        self.nums = []  # 存储元素的数组
        self.val_to_index = {}  # 值到索引的映射

    def insert(self, val: int) -> bool:
        """
        向集合中插入一个元素

        Args:
            val: 要插入的值

        Returns:
            如果元素不存在则插入并返回True，否则返回False
        """
        if val in self.val_to_index:
            return False

        # 插入到数组末尾
        self.nums.append(val)
        # 更新哈希映射
        self.val_to_index[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        从集合中删除一个元素

        Args:
            val: 要删除的值

        Returns:
            如果元素存在则删除并返回True，否则返回False
        """
        if val not in self.val_to_index:
            return False

        # 获取要删除元素的索引
        index_to_remove = self.val_to_index[val]

        # 获取数组最后一个元素
        last_val = self.nums[-1]

        # 将要删除的元素与最后一个元素交换
        self.nums[index_to_remove] = last_val
        # 更新最后一个元素的索引映射
        self.val_to_index[last_val] = index_to_remove

        # 删除最后一个元素（现在是重复的）
        self.nums.pop()
        # 从哈希表中删除val的映射
        del self.val_to_index[val]

        return True

    def getRandom(self) -> int:
        """
        随机返回集合中的一个元素

        Returns:
            随机选择的元素

        Note:
            每个元素被返回的概率相同
        """
        # 从数组中随机选择一个索引
        random_index = random.randint(0, len(self.nums) - 1)
        return self.nums[random_index]

    def __str__(self) -> str:
        """字符串表示"""
        return f"RandomizedSet(size={len(self.nums)}, elements={self.nums})"


# ========== 支持重复元素的扩展版本 ==========
class RandomizedCollection:
    """
    支持重复元素的扩展版本（LeetCode 381: Insert Delete GetRandom O(1) - Duplicates allowed）
    """

    def __init__(self):
        """初始化数据结构"""
        self.nums = []  # 存储元素的数组
        self.val_to_indices = {}  # 值到索引集合的映射

    def insert(self, val: int) -> bool:
        """
        向集合中插入一个元素

        Args:
            val: 要插入的值

        Returns:
            如果元素不存在则返回True，否则返回False
        """
        # 记录是否是新元素
        is_new = val not in self.val_to_indices

        # 插入到数组末尾
        self.nums.append(val)

        # 更新映射
        if is_new:
            self.val_to_indices[val] = set()
        self.val_to_indices[val].add(len(self.nums) - 1)

        return is_new

    def remove(self, val: int) -> bool:
        """
        从集合中删除一个元素

        Args:
            val: 要删除的值

        Returns:
            如果元素存在则删除并返回True，否则返回False
        """
        if val not in self.val_to_indices:
            return False

        # 获取val的一个索引
        index_to_remove = next(iter(self.val_to_indices[val]))

        # 获取数组最后一个元素
        last_val = self.nums[-1]

        # 将要删除的元素与最后一个元素交换
        self.nums[index_to_remove] = last_val

        # 更新索引映射
        # 1. 删除val的索引
        self.val_to_indices[val].remove(index_to_remove)
        if not self.val_to_indices[val]:
            del self.val_to_indices[val]

        # 2. 更新last_val的索引（除非它就是要删除的元素本身）
        if last_val != val:
            self.val_to_indices[last_val].remove(len(self.nums) - 1)
            self.val_to_indices[last_val].add(index_to_remove)

        # 删除数组的最后一个元素
        self.nums.pop()

        return True

    def getRandom(self) -> int:
        """
        随机返回集合中的一个元素

        Returns:
            随机选择的元素
        """
        return random.choice(self.nums)

    def __str__(self) -> str:
        """字符串表示"""
        return f"RandomizedCollection(size={len(self.nums)}, elements={self.nums})"


# ========== 测试用例 ==========
def test_randomized_set():
    """测试RandomizedSet"""
    print("=== 测试 RandomizedSet ===")

    # 测试基本功能
    rs = RandomizedSet()
    print("1. 测试插入:")
    print(f"   insert(1): {rs.insert(1)}")  # True
    print(f"   insert(2): {rs.insert(2)}")  # True
    print(f"   insert(1): {rs.insert(1)}")  # False（重复）
    print(f"   当前状态: {rs}")

    print("\n2. 测试删除:")
    print(f"   remove(2): {rs.remove(2)}")  # True
    print(f"   remove(3): {rs.remove(3)}")  # False（不存在）
    print(f"   当前状态: {rs}")

    print("\n3. 测试随机获取:")
    rs.insert(3)
    rs.insert(4)
    rs.insert(5)
    print(f"   当前状态: {rs}")

    # 多次调用getRandom，统计概率分布
    from collections import Counter
    results = []
    for _ in range(10000):
        results.append(rs.getRandom())

    counter = Counter(results)
    print(f"\n4. 随机性测试（10000次调用）:")
    for val, count in sorted(counter.items()):
        probability = count / 10000
        print(f"   元素 {val}: {count}次, 概率: {probability:.4f}")

    # 测试删除后随机访问的正确性
    print("\n5. 测试删除后的随机访问:")
    print(f"   删除前: {rs}")
    rs.remove(3)
    print(f"   删除3后: {rs}")

    # 验证所有索引映射正确
    print("\n6. 验证索引映射:")
    for i, val in enumerate(rs.nums):
        print(f"   索引 {i}: 值 {val}, 映射验证: {rs.val_to_index[val] == i}")


def test_randomized_collection():
    """测试RandomizedCollection（支持重复元素）"""
    print("\n\n=== 测试 RandomizedCollection ===")

    rc = RandomizedCollection()
    print("1. 插入重复元素:")
    print(f"   insert(1): {rc.insert(1)}")  # True
    print(f"   insert(1): {rc.insert(1)}")  # False（已存在）
    print(f"   insert(2): {rc.insert(2)}")  # True
    print(f"   insert(1): {rc.insert(1)}")  # False（已存在）
    print(f"   当前状态: {rc}")

    print("\n2. 验证重复元素的索引映射:")
    print(f"   val_to_indices: {rc.val_to_indices}")

    print("\n3. 删除元素:")
    print(f"   remove(1): {rc.remove(1)}")  # True
    print(f"   删除后状态: {rc}")
    print(f"   删除后索引映射: {rc.val_to_indices}")

    print("\n4. 随机性测试:")
    results = []
    for _ in range(10000):
        results.append(rc.getRandom())

    counter = Counter(results)
    print("   随机结果统计:")
    for val, count in sorted(counter.items()):
        probability = count / 10000
        print(f"   元素 {val}: {count}次, 概率: {probability:.4f}")


# ========== 进阶：添加更多功能 ==========
class EnhancedRandomizedSet:
    """
    增强版RandomizedSet，添加额外功能
    """

    def __init__(self):
        self.nums = []
        self.val_to_index = {}
        self.operation_count = 0  # 操作计数器

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False

        self.nums.append(val)
        self.val_to_index[val] = len(self.nums) - 1
        self.operation_count += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False

        index_to_remove = self.val_to_index[val]
        last_val = self.nums[-1]

        # 交换并删除
        self.nums[index_to_remove] = last_val
        self.val_to_index[last_val] = index_to_remove
        self.nums.pop()
        del self.val_to_index[val]

        self.operation_count += 1
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)

    def contains(self, val: int) -> bool:
        """检查元素是否存在，O(1)时间"""
        return val in self.val_to_index

    def size(self) -> int:
        """返回元素个数，O(1)时间"""
        return len(self.nums)

    def clear(self) -> None:
        """清空集合，O(1)时间"""
        self.nums.clear()
        self.val_to_index.clear()

    def get_random_k(self, k: int) -> list:
        """
        随机返回k个不重复的元素

        Args:
            k: 要返回的元素个数

        Returns:
            包含k个随机元素的列表

        Raises:
            ValueError: 如果k大于集合大小
        """
        if k > len(self.nums):
            raise ValueError(f"k={k}大于集合大小{len(self.nums)}")

        # 使用Fisher-Yates洗牌算法的一部分
        result = []
        indices = list(range(len(self.nums)))

        for i in range(k):
            # 随机选择一个索引
            j = random.randint(i, len(self.nums) - 1)
            # 交换
            indices[i], indices[j] = indices[j], indices[i]
            result.append(self.nums[indices[i]])

        return result

    def to_list(self) -> list:
        """转换为列表（副本）"""
        return self.nums.copy()

    def __len__(self) -> int:
        """支持len()函数"""
        return len(self.nums)

    def __contains__(self, val: int) -> bool:
        """支持in操作符"""
        return val in self.val_to_index

    def __repr__(self) -> str:
        return f"EnhancedRandomizedSet(size={len(self)}, operations={self.operation_count})"


# ========== 性能测试 ==========
def performance_test():
    """性能测试"""
    print("\n=== 性能测试 ===")
    import time

    # 测试数据量
    test_size = 100000
    operations = 200000

    # 测试EnhancedRandomizedSet
    print(f"测试 {operations} 次操作:")

    rs = EnhancedRandomizedSet()

    # 插入测试
    start = time.time()
    for i in range(test_size):
        rs.insert(i)
    insert_time = time.time() - start
    print(f"  插入 {test_size} 个元素: {insert_time:.4f}秒")

    # 随机访问测试
    start = time.time()
    for _ in range(operations // 2):
        rs.getRandom()
    random_time = time.time() - start
    print(f"  {operations // 2} 次getRandom: {random_time:.4f}秒")

    # 删除测试
    start = time.time()
    for i in range(test_size // 2):
        rs.remove(i)
    remove_time = time.time() - start
    print(f"  删除 {test_size // 2} 个元素: {remove_time:.4f}秒")

    print(f"  最终集合大小: {len(rs)}")
    print(f"  总操作次数: {rs.operation_count}")


# ========== 实际应用示例 ==========
class RandomizedCache:
    """
    实际应用：基于RandomizedSet的缓存实现
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> value
        self.keys = EnhancedRandomizedSet()  # 存储key的随机集合

    def get(self, key: str):
        """获取缓存值"""
        if key in self.cache:
            # 这里我们可以考虑更新key的访问时间（扩展功能）
            return self.cache[key]
        return None

    def put(self, key: str, value) -> None:
        """添加缓存"""
        if key not in self.cache:
            # 检查容量
            if len(self.keys) >= self.capacity:
                # 随机淘汰一个key
                random_key = self.keys.getRandom()
                del self.cache[random_key]
                self.keys.remove(random_key)

            # 添加新key
            self.keys.insert(key)

        # 更新或添加值
        self.cache[key] = value

    def remove(self, key: str) -> bool:
        """删除缓存"""
        if key in self.cache:
            del self.cache[key]
            self.keys.remove(key)
            return True
        return False

    def random_evict(self) -> str:
        """随机淘汰一个缓存项并返回key"""
        if not self.keys:
            raise ValueError("缓存为空")

        random_key = self.keys.getRandom()
        del self.cache[random_key]
        self.keys.remove(random_key)
        return random_key

    def __str__(self):
        return f"RandomizedCache(capacity={self.capacity}, size={len(self.keys)})"


# ========== 主程序 ==========
if __name__ == "__main__":
    print("=" * 60)
    print("Insert Delete GetRandom O(1) - 完整实现")
    print("=" * 60)

    # 运行测试
    test_randomized_set()
    test_randomized_collection()
    performance_test()

    # 演示实际应用
    print("\n=== 实际应用：随机淘汰缓存 ===")
    cache = RandomizedCache(3)

    cache.put("user:1", "Alice")
    cache.put("user:2", "Bob")
    cache.put("user:3", "Charlie")
    print(f"缓存满: {cache}")

    # 再添加一个，会触发随机淘汰
    cache.put("user:4", "David")
    print(f"添加user:4后: {cache}")

    # 获取随机key
    for _ in range(5):
        try:
            key = cache.random_evict()
            print(f"随机淘汰: {key}")
            print(f"  剩余缓存: {cache}")
        except ValueError:
            print("缓存已空")
            break

    print("\n所有测试完成！")
