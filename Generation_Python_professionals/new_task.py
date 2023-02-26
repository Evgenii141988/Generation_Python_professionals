from typing import Generator


def my_range_gen(*args):
    match args:
        case int(stop), :
            step = 1
            start = 0
            while start < stop:
                yield start
                start += step
        case int(start), int(stop):
            step = 1
            while start < stop:
                yield start
                start += step
        case int(start), int(stop), int(step) if (start < stop and step > 0):
            while start < stop:
                yield start
                start += step
        case int(start), int(stop), int(step) if (start > stop and step < 0):
            while start > stop:
                yield start
                start += step
        case _:
            pass


if __name__ == '__main__':
    # for i in my_range_gen(5):
    #     print(i)
    # print()
    # for i in my_range_gen(4, 8):
        # print(i)
    # print()
    # for i in my_range_gen(4, 8, 2):
        # print(i)
    # print()
    for i in my_range_gen(8, 5, -1):
        print(i)
    # print()
    # for i in my_range_gen(4, 8, 0):
    #     print(i)
    #
    # for i in my_range_gen(20, 10, 3):
    #     print(i)
    # # Ничего не печатает, потому что нельзя пройти от 20 до 10 с шагом 3
    #
    # for i in my_range_gen(1, 10, -2):
    #     print(i)
    # for i in range(30, 1, 0):
    #     print(i)

