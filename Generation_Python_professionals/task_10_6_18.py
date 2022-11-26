def interleave(*args):
    return (i for elm in zip(*args) for i in elm)


if __name__ == '__main__':
    print(*interleave('bee', '123'))

    numbers = [1, 2, 3]
    squares = [1, 4, 9]
    qubes = [1, 8, 27]

    print(*interleave(numbers, squares, qubes))