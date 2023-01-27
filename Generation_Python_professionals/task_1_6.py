import pprint

if __name__ == '__main__':
    number = input()
    count = 0
    for i, num in enumerate(number[::-1], 1):
        num = int(num)
        if i % 2 == 0:
            num *= 2
            if num > 9:
                num -= 9
        count += num
    print(count % 10 == 0)

