def get_biggest(numbers: list):
    if numbers:
        str_numbers = [str(i) for i in numbers]
        for i in range(len(numbers)):
            index = i
            for j in range(i + 1, len(numbers)):
                if str_numbers[j] + str_numbers[index] > str_numbers[index] + str_numbers[j]:
                    index = j
            str_numbers[i], str_numbers[index] = str_numbers[index], str_numbers[i]
        return int(''.join(str_numbers))
    return -1


if __name__ == '__main__':
    print(get_biggest([1, 2, 3]))
    print(get_biggest([61, 228, 9, 3, 11]))
    print(get_biggest([7, 71, 72]))
    print(get_biggest([]))
    print(get_biggest([3]))
    print(get_biggest([0, 0, 0, 0, 0, 0]))
    print(get_biggest([13, 221, 423, 53, 1, 2, 33, 58, 78554, 34, 65, 65, 2, 1]))
