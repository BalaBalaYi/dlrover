"""快速排序"""

def sort(arr):
    if len(arr) <= 1:
        return arr

    mid_value = arr[len(arr)//2]

    left = [x for x in arr if x < mid_value]
    middle = [x for x in arr if x == mid_value]
    right = [x for x in arr if x > mid_value]

    return sort(left) + middle + sort(right)


if __name__ == '__main__':
    print(sort([6, 7, 3, 1, 2, 5]))
