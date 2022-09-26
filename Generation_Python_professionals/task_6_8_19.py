from collections import Counter


def print_bar_chart(data: (list, str), mark: str) -> None:
    n = len(max(data, key=len))
    new_data = sorted([elem for elem in Counter(data).items()], key=lambda x: x[1], reverse=True)
    for elem, total in new_data:
        print(f'{elem}{(n - len(elem)) * " "} |{total * mark}')


if __name__ == '__main__':
    print_bar_chart('beegeek', '+')

    languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']
    print_bar_chart(languages, '#')