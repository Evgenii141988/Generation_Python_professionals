from collections import OrderedDict


def custom_sort(ordered_dict: OrderedDict, by_values: bool = False) -> None:
    values = sorted(ordered_dict, key=lambda x: ordered_dict[x] if by_values else x)
    for value in values:
        ordered_dict.move_to_end(value)


if __name__ == '__main__':
    data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
    custom_sort(data)
    print(data)
    data1 = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
    custom_sort(data1, by_values=True)

    print(*data1.items())