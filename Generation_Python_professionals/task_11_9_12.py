import re

if __name__ == '__main__':
    a, b = map(int, input().split())
    string = input()
    reg = re.compile(r'\d+')
    print(sum(map(int, reg.findall(string, pos=a, endpos=b))))
