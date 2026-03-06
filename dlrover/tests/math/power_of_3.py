"""判断一个数字是否是3 的次方。"""

def is_power_of_3(n):
    if n <= 0:
        return False

    while n % 3 == 0:
        n //= 3

    return n == 1
