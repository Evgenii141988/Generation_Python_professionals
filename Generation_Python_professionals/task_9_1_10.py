def my_pow(number: int):
    return sum([pow(int(elm), i)for i, elm in enumerate(str(number), 1)])


if __name__ == '__main__':
    print(my_pow(139))
    print(my_pow(123))
    print(my_pow(0))
