"""给定一个数字n，求小于n 的质数的个数。

输入: n = 10
输出: 4
解释: 小于 10 的质数有 2, 3, 5, 7

核心：埃拉托斯特尼筛法（Sieve of Eratosthenes）

这是计算质数数量的经典高效算法。

算法步骤：
创建布尔数组 is_prime[0..n-1]，初始全为 True
0 和 1 不是质数，标记为 False
从 2 开始遍历到 √n：
如果 is_prime[i]是 True，则 i是质数
将 i的所有倍数标记为 False
统计 is_prime中 True的数量
优化技巧：
外层循环只需到 √n
内层循环从 i*i开始
步长为 i
"""


def solve(n):
    if n <= 2:
        return 0

    # 初始结果集
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    # 只需要检查到 根号n
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            # key
            for j in range(i * i, n, i):
                is_prime[j] = False

    return sum(is_prime)
