from collections import Counter


def make_header(text: str, n: int = 1) -> str:
    return f'<h{n}>{text}</h{n}>'


if __name__ == '__main__':
    print(make_header('Нет'))
    print(make_header('Bella Ciao', 4))
    print(make_header('Go little rock star', 6))
    print(make_header('Девальвации не будет. Твердо и четко'))
