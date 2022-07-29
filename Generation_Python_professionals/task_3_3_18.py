from datetime import datetime


def is_available_date(booked_dates: list, date_for_booking: str) -> bool:
    new_booked_dates = []
    for my_date in booked_dates:
        if len(my_date) == 10:
            new_booked_dates.append(datetime.strptime(my_date, '%d.%m.%Y').toordinal())
        else:
            start, end = [datetime.strptime(d, '%d.%m.%Y').toordinal() for d in my_date.split('-')]
            new_booked_dates += [d for d in range(start, end + 1)]
    if len(date_for_booking) == 10:
        date_set = {datetime.strptime(date_for_booking, '%d.%m.%Y').toordinal()}
    else:
        start, end = [datetime.strptime(d, '%d.%m.%Y').toordinal() for d in date_for_booking.split('-')]
        date_set = {d for d in range(start, end + 1)}
    if set(new_booked_dates) & date_set:
        return False
    return True


if __name__ == '__main__':
    dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
    some_date = '10.11.2021-14.11.2021'
    print(is_available_date(dates, some_date))