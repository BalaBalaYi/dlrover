"""给定一些二维坐标中的点，求同一条线上最多由多少点。
"""


def maxPoints(points):
    """
    计算二维平面上同一条直线上最多的点数
    :param points: List[List[int]] 点坐标列表
    :return: int 最大点数
    """
    n = len(points)
    if n <= 2:
        return n  # 少于3个点，直接返回

    max_count = 0
    for i in range(n):
        # 以点i为基准，统计所有经过i的直线
        slope_count = {}
        same_point = 0  # 记录与i重合的点数
        current_max = 0

        for j in range(i + 1, n):
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]

            # 处理重合点
            if dx == 0 and dy == 0:
                same_point += 1
                continue

            # 计算斜率（用最简分数表示，避免浮点精度问题）
            gcd_val = gcd(dx, dy)
            dx //= gcd_val
            dy //= gcd_val

            # 统一斜率表示（确保符号一致）
            if dx < 0:
                dx, dy = -dx, -dy

            slope = (dx, dy)
            slope_count[slope] = slope_count.get(slope, 0) + 1
            current_max = max(current_max, slope_count[slope])

        # 更新最大值：当前直线上的点 + 基准点 + 重合点
        max_count = max(max_count, current_max + same_point + 1)

    return max_count


def gcd(a, b):
    """计算最大公约数"""
    while b:
        a, b = b, a % b
    return a
