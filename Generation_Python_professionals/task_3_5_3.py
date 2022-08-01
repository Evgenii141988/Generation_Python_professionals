from datetime import timedelta, datetime

if __name__ == '__main__':
    week_work_hours = {
        0: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
        1: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
        2: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
        3: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
        4: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
        5: {'start': timedelta(hours=10), 'end': timedelta(hours=18)},
        6: {'start': timedelta(hours=10), 'end': timedelta(hours=18)}
    }
    pattern = '%d.%m.%Y %H:%M'
    my_date = datetime.strptime(input(), pattern)
    my_time = timedelta(hours=my_date.hour, minutes=my_date.minute)
    if week_work_hours[my_date.weekday()]['start'] <= my_time < week_work_hours[my_date.weekday()]['end']:
        print((week_work_hours[my_date.weekday()]['end'] - my_time).seconds // 60)
    else:
        print('Магазин не работает')