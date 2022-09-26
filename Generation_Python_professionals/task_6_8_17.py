import csv
from collections import Counter

if __name__ == '__main__':
    with open('name_log.csv', encoding='utf-8') as file:
        users = Counter(sorted([user['email'] for user in csv.DictReader(file)]))
    print(*[f'{email}: {total}' for email, total in users.items()], sep='\n')
