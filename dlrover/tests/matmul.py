from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List


def matmul_multi_thread(a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
    m = len(a)
    n = len(a[0])
    p = len(b[0])

    c: List[List[float]] = [[0] * p for _ in range(m)]

    def multiple(i: int, j: int):
        total = 0.0
        for k in range(n):
            total += a[i][k] * b[k][j]
        return i, j, total

    with ThreadPoolExecutor(max_workers=m) as executor:
        futures = []
        for i in range(m):
            for j in range(p):
                futures.append(executor.submit(multiple, i, j))

        for future in as_completed(futures):
            i, j, value = future.result()
            c[i][j] = value

    return c


if __name__ == '__main__':
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[1, 4], [2, 5], [3, 6]]
    print(matmul_multi_thread(a, b))  # [[14.0, 32.0], [32.0, 77.0]]
