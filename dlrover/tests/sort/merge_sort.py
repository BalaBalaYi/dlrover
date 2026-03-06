"""归并排序"""

def sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left_arr, right_arr):
        i, j = 0, 0
        sorted_array = []

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                sorted_array.append(left_arr[i])
                i += 1
            else:
                sorted_array.append(right_arr[j])
                j += 1

        sorted_array.extend(left_arr[i:])
        sorted_array.extend(right_arr[j:])

        return sorted_array

    n = len(arr)
    mid = n // 2

    left = arr[:mid]
    right = arr[mid:]

    left_result = sort(left)
    right_result = sort(right)

    return merge(left_result, right_result)


if __name__ == '__main__':
    print(sort([6, 7, 3 , 1, 2, 5]))
