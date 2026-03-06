"""给定一个数组 prices，它的第 i个元素 prices[i]表示一支给定股票第 i天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
如果你不能获取任何利润，返回 0。

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5。
     注意利润不能是 7-1 = 6，因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
"""


def solve(prices):
    max_profit = 0
    if not prices:
        return max_profit

    last_price = -1
    for price in prices:
        if last_price != -1 and price > last_price:
            max_profit = max(max_profit, price - last_price)
        last_price = price

    return max_profit

if __name__ == '__main__':
    print(solve([7,1,5,3,6,4]))  # 4
    print(solve([7,6,4,3,1]))  # 0
