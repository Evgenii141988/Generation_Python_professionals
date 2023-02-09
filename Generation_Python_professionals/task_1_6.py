if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n - 2, -1, -1):
        for j in range(m - 2, -1, -1):
            matrix[i][j] = matrix[i][j + 1] + matrix[i + 1][j]
    for row in matrix:
        print(*row, sep=' ')
