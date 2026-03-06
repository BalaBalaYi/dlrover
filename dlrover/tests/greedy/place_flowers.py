"""
假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
给你一个整数数组 flowerbed表示花坛，由若干 0和 1组成，其中 0表示没种植花，1表示种植了花。另有一个数 n，
要求判断能否在不打破种植规则的情况下种入 n朵花。能则返回 true，不能则返回 false。

输入: flowerbed = [1,0,0,0,1], n = 1
输出: true
解释: 在第一个和最后一个花之间种一朵花
"""

"""
核心思想：

遍历花坛，对于每个位置：
1. 如果当前位置已经有花（flowerbed[i] == 1），跳过
2. 如果当前位置为空（flowerbed[i] == 0），检查左右是否都为空
3. 如果是，可以种花，计数加一，并将该位置标记为有花

"""


def solve(flowerbed, n):
    length = len(flowerbed)
    count = 0
    i = 0

    while i < length:
        # 如果当前位置已经有花，跳过
        if flowerbed[i] == 1:
            i += 2
        else:
            # 检查是否可以种花
            left_empty = (i == 0) or (flowerbed[i - 1] == 0)
            right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)

            if left_empty and right_empty:
                # 可以种花
                flowerbed[i] = 1
                count += 1
                i += 2
            else:
                i += 1

    return count >= n