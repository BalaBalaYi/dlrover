import heapq


def findKthLargest_heap(nums, k):
    """使用heap找到第k大的元素"""
    if k > len(nums):
        raise RuntimeError()

    heap = []
    heapq.heapify(heap)

    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            if num >= heap[0]:
                heapq.heapreplace(heap, num)

    return heap[0]


def findKthLargest(nums, k):
    """
    使用快速选择找到第k大的元素
    :param nums: 未排序数组
    :param k: 第k大（k从1开始）
    :return: 第k大的元素
    """

    def partition(left, right, pivot_idx):
        """分区函数，返回基准元素的最终位置"""
        pivot_value = nums[pivot_idx]

        # 1. 将基准元素移到末尾
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

        # 2. 分区：将小于基准的移到左边
        store_idx = left
        for i in range(left, right):
            if nums[i] < pivot_value:
                nums[store_idx], nums[i] = nums[i], nums[store_idx]
                store_idx += 1

        # 3. 将基准元素移到正确位置
        nums[store_idx], nums[right] = nums[right], nums[store_idx]

        return store_idx

    def select(left, right, k_smallest):
        """在[left, right]范围内寻找第k_smallest小的元素"""
        if left == right:  # 只有一个元素
            return nums[left]

        # 选择基准（这里选择中间元素）
        pivot_idx = left + (right - left) // 2

        # 分区并获取基准的最终位置
        pivot_idx = partition(left, right, pivot_idx)

        # 判断目标在哪一边
        if k_smallest == pivot_idx:
            return nums[k_smallest]
        elif k_smallest < pivot_idx:
            return select(left, pivot_idx - 1, k_smallest)
        else:
            return select(pivot_idx + 1, right, k_smallest)

    # 第k大 = 第(n-k)小（因为k从1开始，索引从0开始）
    n = len(nums)
    return select(0, n - 1, n - k)


if __name__ == "__main__":
    # 测试
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(f"数组: {nums}")
    print(f"第{k}大的数是: {findKthLargest(nums.copy(), k)}")  # 输出 5
    print(f"第{k}大的数是: {findKthLargest_heap(nums.copy(), k)}")  # 输出 5