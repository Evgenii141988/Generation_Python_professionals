import csv
from collections import namedtuple
from datetime import datetime

if __name__ == '__main__':
    pattern_date = '%d.%m.%Y'
    pattern_time = '%H:%M'
    Guest = namedtuple('Guest', ['surname', 'name', 'meeting_date', 'meeting_time'])
    guests = []
    with open('meetings.csv', 'r', encoding='utf-8') as file:
        rows = csv.DictReader(file)
        for row in rows:
            guests.append(Guest(row['surname'], row['name'], datetime.strptime(row['meeting_date'], pattern_date), datetime.strptime(row['meeting_time'], pattern_time)))
    guests.sort(key=lambda x: (x.meeting_date, x.meeting_time))
    for guest in guests:
        print(f'{guest.surname} {guest.name}')