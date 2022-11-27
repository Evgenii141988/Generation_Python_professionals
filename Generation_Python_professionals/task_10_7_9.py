def nonempty_lines(file: str):
    with open(file, 'r', encoding='utf-8') as file_out:
        return (line.strip() if len(line.strip()) <= 25 else '...' for line in file_out.readlines() if line.strip() != '')


if __name__ == '__main__':
    lines = nonempty_lines('diary.txt')

    print(next(lines))
    print(next(lines))
    print(next(lines))