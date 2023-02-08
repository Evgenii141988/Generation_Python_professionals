
def create_actor(data: dict = {'name': 'Райан', 'surname': 'Рейнольдс', 'age': 46}, **kwargs) -> dict:
    return data | kwargs


if __name__ == '__main__':
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    result = [matrix[i][j] for i in range(n) for j in range(n) if i + j == n - 1]
    print(max(result))
