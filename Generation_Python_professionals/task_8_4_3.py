def recursive_sum(nested_lists: list):
    total = 0
    for elem in nested_lists:
        if type(elem) == int:
            total += elem
        else:
            total += recursive_sum(elem)
    return total


def recursive_sum1(nested_lists: list):
    total = 0

    def rec(numbers):
        nonlocal total
        for elem in numbers:
            if type(elem) == int:
                total += elem
            else:
                rec(elem)
        return total

    return rec(nested_lists)


if __name__ == '__main__':
    # my_list = [1, [4, 4], 2, [1, [2, 10]]]
    my_list = []

    print(recursive_sum(my_list))
