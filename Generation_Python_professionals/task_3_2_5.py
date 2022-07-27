from datetime import date


if __name__ == '__main__':
    birthday = date(1992, 10, 6)

    print('Название месяца:', birthday.strftime('%B'))
    print('Название дня недели:', birthday.strftime('%A'))
    print('Год:', birthday.strftime('%Y'))
    print('Месяц:', birthday.strftime('%m'))
    print('День:', birthday.strftime('%d'))