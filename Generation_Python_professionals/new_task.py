def find_lines_len_more_6(file_name: str) -> int:
    with open(file_name, 'r', encoding='utf-8') as file:
        strings = [line.strip() for line in file.readlines() if len(line.strip()) > 6]
        return len(strings)


if __name__ == '__main__':
