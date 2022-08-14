import csv
from datetime import datetime

if __name__ == '__main__':
    patter = '%d/%m/%Y %H:%M'
    columns = ['username', 'email', 'dtime']
    data = []
    with open('name_log.csv', 'r', encoding='utf-8') as file:
        rows = list(csv.DictReader(file))
        emails = {row['email'] for row in rows}
        for email in emails:
            user = [row for row in rows if row['email'] == email]
            last_user = max(user, key=lambda x: datetime.strptime(x['dtime'], patter))
            data.append([last_user['username'], last_user['email'], last_user['dtime']])
    data.sort(key=lambda x: x[1])
    with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerows(data)