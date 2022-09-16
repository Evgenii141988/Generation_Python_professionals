from collections import defaultdict


def wins(obj):
    name_wins = defaultdict(set)
    for k, v in obj:
        name_wins[k].add(v)
    return name_wins


if __name__ == '__main__':
    result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Артур', 'Дима')])

    for winner, losers in sorted(result.items()):
        print(winner, '->', *sorted(losers))