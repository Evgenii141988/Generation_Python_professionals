def linear(nested_lists: list) -> list:
    result_list = []

    def rec(elements):
        if type(elements) == int:
            result_list.append(elements)
        if type(elements) == list:
            for elem in elements:
                rec(elem)

    rec(nested_lists)
    return result_list


if __name__ == '__main__':
    my_list = [3, [4], [5, [6, [7, 8]]]]

    print(linear(my_list))

    my_list = [10, 20, 30, 40, 50]

    print(linear(my_list))