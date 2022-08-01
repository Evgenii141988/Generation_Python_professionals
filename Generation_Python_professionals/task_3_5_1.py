from datetime import date, time, datetime, timedelta

if __name__ == '__main__':
    data = [('07:14', '08:46'),
            ('09:01', '09:37'),
            ('10:00', '11:43'),
            ('12:13', '13:49'),
            ('15:00', '15:19'),
            ('15:58', '17:24'),
            ('17:57', '19:21'),
            ('19:30', '19:59')]
    total = 0
    patern = '%H:%M'
    for my_date in data:
        start, end = [datetime.strptime(d, patern) for d in my_date]
        total += (end - start).seconds // 60
    print(total)
