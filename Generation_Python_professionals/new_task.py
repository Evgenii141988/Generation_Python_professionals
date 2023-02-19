def file_n_lines(file_name: str, n: int) -> None:
    with open(file_name, 'r', encoding='utf-8') as file:
        strings = [string.strip() for string in file.readlines()]
        for string in strings[:n]:
            print(string)

if __name__ == '__main__':

