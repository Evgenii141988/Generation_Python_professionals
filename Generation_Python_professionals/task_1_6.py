import pprint

if __name__ == '__main__':
    n = int(input())
    len_list = [len(set(list(map(int, input().split())))) for _ in range(n)]
    print(*len_list, sep='\n')