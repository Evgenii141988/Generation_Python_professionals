from itertools import product


def password_gen1():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                yield str(i) + str(j) + str(k)


def password_gen():
    return (f'{elm[0]}{elm[1]}{elm[2]}' for elm in product(range(10), repeat=3))


if __name__ == '__main__':
    for elm in password_gen():
        print(elm)
