import csv

if __name__ == '__main__':
    n = int(input())
    with open('deniro.csv', 'r', encoding='utf-8') as file:
        rows = csv.reader(file)
        sort_rows = sorted(rows, key=lambda x: int(x[n - 1]) if x[n - 1].isdigit() else x[n - 1])
        for row in sort_rows:
            print(*row, sep=',')
