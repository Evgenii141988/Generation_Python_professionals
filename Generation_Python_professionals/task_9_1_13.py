def get_sorted_strings(string: str) -> str:
    lower_lit = sorted([lit for lit in string if lit.islower()])
    upper_lit = sorted([lit for lit in string if lit.isupper()])
    even_num = sorted([lit for lit in string if lit.isdigit() and int(lit) % 2 == 0])
    odd_num = sorted([lit for lit in string if lit.isdigit() and int(lit) % 2 != 0])
    return ''.join(lower_lit + upper_lit + odd_num + even_num)


if __name__ == '__main__':
    print(get_sorted_strings(input()))
    print(get_sorted_strings('Sorting1234'))
    print(get_sorted_strings('n0tEast3rEgg'))
    print(get_sorted_strings('3DYrz34UXl'))
