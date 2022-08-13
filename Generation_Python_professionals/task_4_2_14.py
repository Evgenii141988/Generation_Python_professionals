import csv


def csv_columns(filename: str) -> dict:
    result = {}
    with open(filename, 'r', encoding='utf-8') as file:
        rows = csv.DictReader(file)
        for row in rows:
            keys = list(row)
            for key in keys:
                result[key] = result.get(key, []) + [row[key]]
    return result


if __name__ == '__main__':
    print(csv_columns('writing_test.csv'))
