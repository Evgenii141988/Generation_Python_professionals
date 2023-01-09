def cmp_prev(val, numbers=[]):
    if len(numbers) < 1:
        numbers.append(val)
        return False
    flag = val > sum(numbers[-2:])
    numbers.append(val)
    return flag


if __name__ == '__main__':
    print(cmp_prev(0))  # False
    print(cmp_prev(1))  # True
    print(cmp_prev(68))  # True
    print(cmp_prev(57))  # False
    print(cmp_prev(346))  # True
    print(cmp_prev(4))  # False
    print(cmp_prev(5))  # False
    print(cmp_prev(10))  # True
    print(cmp_prev(15))  # False
    print(cmp_prev(-7))  # False
    print(cmp_prev(8))  # False
    print(cmp_prev(2))  # True
    print(cmp_prev(-6))  # False
    print(cmp_prev(-7))  # False
    print(cmp_prev(-6))  # True
    print(cmp_prev(0))  # True
    print(cmp_prev(-5))  # True
    print(cmp_prev(65))  # True
    print(cmp_prev(456))  # True
    print(cmp_prev(-678))  # False
    print(cmp_prev(77))  # True
